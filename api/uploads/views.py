import os
import tempfile
import magic
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from .tasks import process_uploaded_file
from datetime import datetime

AUDIO_MPEG = "audio/mpeg"
SAVE_DIR = "/Users/dave/projects/music-player/cdn/temp"


class UploadView(ViewSet):
    def list(self):
        return Response("GET API")

    def check_file_type(self, file_uploaded):
        temp_file = tempfile.NamedTemporaryFile(delete=True)
        for chunk in file_uploaded.chunks():
            temp_file.write(chunk)

        mime = magic.Magic(mime=True)
        file_type = mime.from_file(temp_file.name)

        temp_file.close()

        return AUDIO_MPEG in file_type

    def save_file_locally(self, file_uploaded):
        os.makedirs(SAVE_DIR, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = f"{timestamp}_{file_uploaded.name}"
        destination_path = os.path.join(SAVE_DIR, file_name)

        with open(destination_path, 'wb') as destination_file:
            for chunk in file_uploaded.chunks():
                destination_file.write(chunk)

        return destination_path

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')

        if not file_uploaded:
            return Response("No file uploaded", status=status.HTTP_400_BAD_REQUEST)

        if not file_uploaded.name.lower().endswith('.mp3'):
            return Response("File is not an MP3. Incorrect file extension.", status=status.HTTP_400_BAD_REQUEST)

        if self.check_file_type(file_uploaded):
            temp_path = self.save_file_locally(file_uploaded)
            process_uploaded_file.delay(temp_path, "dave")

            response = f"File uploaded successfully {temp_path}."
            return Response(response)
        else:
            response = f"File is not an MP3."
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

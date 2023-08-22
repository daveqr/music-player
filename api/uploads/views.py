import os
import tempfile
import magic
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet

AUDIO_MPEG = "audio/mpeg"


class UploadView(ViewSet):
    def list(self):
        return Response("GET API")

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')

        if not file_uploaded:
            return Response("No file uploaded", status=status.HTTP_400_BAD_REQUEST)

        if not file_uploaded.name.lower().endswith('.mp3'):
            return Response("File is not an MP3. Incorrect file extension.", status=status.HTTP_400_BAD_REQUEST)

        temp_file = None

        temp_file = tempfile.NamedTemporaryFile(delete=True)
        for chunk in file_uploaded.chunks():
            temp_file.write(chunk)

        mime = magic.Magic(mime=True)
        file_type = mime.from_file(temp_file.name)

        if AUDIO_MPEG in file_type:
            response = f"File uploaded successfully: {file_type}"
            return Response(response)
        else:
            response = f"File is not an MP3. Detected type: {file_type}"
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

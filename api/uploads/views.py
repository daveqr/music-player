from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
import magic
import tempfile


class UploadView(ViewSet):
    def list(self):
        return Response("GET API")

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')

        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            for chunk in file_uploaded.chunks():
                temp_file.write(chunk)

        mime = magic.Magic(mime=True)
        file_type = mime.from_file(temp_file.name)

        if "audio/mpeg" in file_type:
            response = f"File uploaded successfully: {file_type}"
            return Response(response)
        else:
            response = f"File is not an MP3. Detected type: {file_type}"
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        # response = f"File uploaded successfully {file_type}".format(
        #     file_type)
        # return Response(response)

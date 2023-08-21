from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet


class UploadView(ViewSet):
    def list(self):
        return Response("GET API")

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        content_type = file_uploaded.content_type
        response = f"File uploaded successfully {content_type}".format(
            content_type)
        return Response(response)

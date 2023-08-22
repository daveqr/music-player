from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
import os

TESTDATA_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__), 'testdata'))


class UploadViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_upload_mp3_file(self):
        filename = os.path.join(TESTDATA_DIR, 'aaa.mp3')

        with open(filename, 'rb') as file:
            file_content = file.read()

        mp3_uploaded = SimpleUploadedFile(
            "file.mp3", file_content)

        response = self.client.post(
            "/upload/", {"file_uploaded": mp3_uploaded}, format="multipart")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("File uploaded successfully", str(response.data))

    def test_upload_non_mp3_file(self):
        filename = os.path.join(TESTDATA_DIR, 'text.txt')

        with open(filename, 'rb') as file:
            file_content = file.read()

        text_file = SimpleUploadedFile(
            "file.txt", file_content)

        response = self.client.post(
            '/upload/', {'file_uploaded': text_file}, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("File is not an MP3", str(response.data))

    def test_upload_no_file(self):
        response = self.client.post('/upload/')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("No file uploaded", str(response.data))

    def test_upload_invalid_file_format(self):
        # invalide_format.txt is an mp3 with a txt extension
        filename = os.path.join(TESTDATA_DIR, 'invalid_format.txt')

        with open(filename, 'rb') as file:
            file_content = file.read()

        invalid_file = SimpleUploadedFile(
            "invalid_format.txt", file_content, content_type="audio/mpeg")

        response = self.client.post(
            "/upload/", {"file_uploaded": invalid_file}, format="multipart")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEquals(
            "File is not an MP3. Incorrect file extension.", str(response.data))

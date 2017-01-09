from django.test import TestCase
import os
from rest_framework import status


class ImageUploadTestCase(TestCase):

    def test_upload_image(self):
        path_to_image = os.path.join('imageuploads','files_to_upload', 'first_file.jpg')
        data = {
            'file': open(path_to_image, 'rb')
        }
        url = 'http://localhost:8080/upload/'
        response = self.client.post(url, data, format='multipart')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
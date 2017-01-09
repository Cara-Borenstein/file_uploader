from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from io import FileIO, BufferedWriter
from .models import Upload


class UploadList(APIView):
    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request):
        upload = request.FILES['file']

        name = upload.name
        upload_folder = 'uploads'
        filename = '{upload_folder}/{name}'.format(upload_folder=upload_folder, name=name)

        with BufferedWriter(FileIO(filename, 'w')) as dest:
            for c in upload.chunks():
                dest.write(c)

        upload = Upload.objects.create(
            url="http://localhost:8080/uploads/{filename}".format(filename=filename),
            path_to_image=filename
        )
        return Response(data="Uploaded image {filename} at time {created}".format(filename=filename,
                                                                                  created=upload.created)
                        , status=status.HTTP_201_CREATED)

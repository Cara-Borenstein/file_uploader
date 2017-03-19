from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework import renderers
from io import FileIO, BufferedWriter
from .models import Upload, UploadEnvelope


class JPEGRenderer(renderers.BaseRenderer):
    media_type = 'image/jpeg'
    format = 'jpg'
    charset = None
    render_style = 'binary'

    def render(self, data, media_type=None, renderer_context=None):
        return data


#  curl -X POST localhost:8080/upload/ -F 'file=@imageuploads/files_to_upload/first_file.jpg'
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


class UploadEnvelopeList(APIView):
    parser_classes = (MultiPartParser, FormParser,)


    def post(self, request):
        upload = request.FILES['file']

        name = upload.name
        upload_folder = 'imageuploads/static' #''uploads'
        filename = '{upload_folder}/{name}'.format(upload_folder=upload_folder, name=name)

        with BufferedWriter(FileIO(filename, 'w')) as dest:
            for c in upload.chunks():
                dest.write(c)

        upload = Upload.objects.create(
            url="http://localhost:8080/static/{filename}".format(filename=filename),
            path_to_image=filename
        )

        upload_envelope = UploadEnvelope.objects.create(
            image=upload, name='My Envelope'
        )


        return Response(data="Uploaded image {filename} with name {name}".format(filename=upload_envelope.image.path_to_image, name=upload_envelope.name))


class UploadDetailView(APIView):
    renderer_classes = (JPEGRenderer, )

    def get(self, request):
        image = '/Users/cara/Projects/Playground/fileuploader/uploads/first_file.jpg '
        # this will be a db property http://stackoverflow.com/questions/26621114/django-rest-api-to-expose-images
        return Response(data=image) #,content_type="image/jpeg")

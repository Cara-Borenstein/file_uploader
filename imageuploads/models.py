from django.db import models
#from django_extensions.db.models import TimeStampedModel


class Upload(models.Model):
    path_to_image = models.CharField(null=True, max_length=100)
    datafile = models.FileField(null=True)
    url = models.URLField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class UploadEnvelope(models.Model):
    image = models.ForeignKey(Upload)
    name = models.CharField(null=True, max_length=50)
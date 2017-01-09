from rest_framework import serializers
from .models import Upload


class UploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Upload
        read_only_fields = ('created', 'modified','url')

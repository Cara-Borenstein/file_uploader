from rest_framework import serializers
from .models import Upload, UploadEnvelope


class UploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Upload
        read_only_fields = ('created', 'modified', 'url')


class UploadEnvelopeSerializer(serializers.ModelSerializer):

    class Meta:
        model = UploadEnvelope
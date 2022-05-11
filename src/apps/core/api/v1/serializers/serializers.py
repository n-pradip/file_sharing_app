from rest_framework import serializers
from src.apps.core.models import FileModel


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileModel
        fields = ['id', 'file']
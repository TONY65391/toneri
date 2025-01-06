from rest_framework import serializers
from .models import MODELS

class SERIALIZER(serializers.ModelSerializer):
    class Meta:
        model = MODELS()
        fields = "__all__"
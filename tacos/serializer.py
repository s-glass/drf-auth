from rest_framework import serializers
from .models import Taco


class TacoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'owner', 'name', 'meat', 'description', 'updated_at', 'created_at')
        model = Taco
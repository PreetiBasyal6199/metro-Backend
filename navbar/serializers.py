from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import navbar_items,background_hero
class navitem_serializer(serializers.ModelSerializer):
    class Meta:
        model=navbar_items
        fields=['navText','link']

class backgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model=background_hero
        fields="__all__"
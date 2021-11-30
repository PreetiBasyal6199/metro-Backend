from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import navbar_items
class navitem_serializer(serializers.ModelSerializer):
    class Meta:
        model=navbar_items
        fields=['navText','link']
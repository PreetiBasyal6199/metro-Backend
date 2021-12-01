from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import navbar_items,background_hero,services,why_metro
class navitem_serializer(serializers.ModelSerializer):
    class Meta:
        model=navbar_items
        fields=['navText','link']

class backgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model=background_hero
        fields="__all__"


class serviceSerializer(serializers.ModelSerializer):
    service_image=serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model=services
        fields=['id','service_title','service_image','service_description']


class why_metroSerializer(serializers.ModelSerializer):
    class Meta:
        model=why_metro
        fields=['id','why_head','why_content']
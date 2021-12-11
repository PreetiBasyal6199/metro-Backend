from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import navbar_items,background_hero,services,why_metro,customer_review,get_in_touch_items,footer_items
class navitem_serializer(serializers.ModelSerializer):
    class Meta:
        model=navbar_items
        fields=['navText','link']

class backgroundSerializer(serializers.ModelSerializer):
    background_img=serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model=background_hero
        fields=['background_img','background_title','background_stitle','button_name']


class why_metroSerializer(serializers.ModelSerializer):
    class Meta:
        model=why_metro
        fields=['why_head','why_content']

class serviceSerializer(serializers.ModelSerializer):
    service_image=serializers.FileField(max_length=None,use_url=True)
    class Meta:
        model=services
        fields=['service_title','service_image','service_description']

class customer_reviewSerializer(serializers.HyperlinkedModelSerializer):
    reviewer_image=serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model=customer_review
        fields=['review_details','reviewer_name','reviewer_image']

class get_in_touchSerializer(serializers.ModelSerializer):
    social_media_img=serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model=get_in_touch_items
        fields=['social_media_img',]

class footerserializer(serializers.ModelSerializer):
    class Meta:
        model=footer_items
        fields="__all__"



    
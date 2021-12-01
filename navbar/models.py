from django.db import models
from rest_framework.serializers import ModelSerializer

# Create your models here.
class navbar_items(models.Model):
    navText=models.CharField(max_length=50)
    link=models.CharField(max_length=100,blank=True)


    def __str__(self):
        return self.navText


class background_hero(models.Model):
    background_img=models.ImageField(upload_to="images")
    background_title=models.CharField(max_length=100)
    background_stitle=models.CharField(max_length=50)
    button_name=models.CharField(max_length=25)


class services(models.Model):
    service_image=models.ImageField(upload_to="services")
    service_title=models.CharField(max_length=25)
    service_description=models.CharField(max_length=250)

class why_metro(models.Model):
    why_head=models.CharField(max_length=50)
    why_content=models.CharField(max_length=500)
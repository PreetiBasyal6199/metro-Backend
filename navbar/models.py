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

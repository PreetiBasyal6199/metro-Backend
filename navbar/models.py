from django.db import models
from rest_framework.serializers import ModelSerializer

# Create your models here.
class navbar_items(models.Model):
    navText=models.CharField(max_length=50)
    link=models.CharField(max_length=100,blank=True)


    def __str__(self):
        return self.navText


class background_hero(models.Model):
    background_img=models.ImageField()
    background_title=models.CharField(max_length=100)
    background_stitle=models.CharField(max_length=50)
    button_name=models.CharField(max_length=25)

    def __str__(self):
        return self.background_title


class why_metro(models.Model):
    why_head=models.CharField(max_length=50)
    why_content=models.CharField(max_length=500)

    def __str__(self):
        return self.why_head

class services(models.Model):
    service_image=models.FileField()
    service_title=models.CharField(max_length=25)
    service_description=models.CharField(max_length=1000)

    def __str__(self):
        return self.service_title



class customer_review(models.Model):
    review_details=models.CharField(max_length=500)
    reviewer_name=models.CharField(max_length=50)
    reviewer_image=models.ImageField()

    def __str__(self):
        return self.reviewer_name


class get_in_touch_items(models.Model):
    social_media_name=models.CharField(max_length=50)
    social_media_img=models.ImageField()
    def __str__(self):
        return self.social_media_name

class footer_items(models.Model):
    footer_head=models.CharField(max_length=50)
    metro_address=models.CharField(max_length=100)
    metro_phn=models.CharField(max_length=20)
    copyright_details=models.CharField(max_length=50)
    other_details=models.CharField(max_length=100)

    def __str__(self):
        return self.footer_head




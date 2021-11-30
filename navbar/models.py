from django.db import models

# Create your models here.
class navbar_items(models.Model):
    navText=models.CharField(max_length=50)
    link=models.CharField(max_length=100)


    def __str__(self):
        return self.nav_title
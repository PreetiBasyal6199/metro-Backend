from django.db import models

# Create your models here.
class navbar_items(models.Model):
    nav_title=models.CharField(max_length=50)
    nav_link=models.URLField(max_length=100)


    def __str__(self):
        return self.nav_title
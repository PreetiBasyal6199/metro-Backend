# Generated by Django 3.2.9 on 2021-12-01 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navbar', '0003_background_hero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='background_hero',
            name='background_img',
            field=models.ImageField(upload_to='images/'),
        ),
    ]

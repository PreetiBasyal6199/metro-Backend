# Generated by Django 3.2.9 on 2021-12-02 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navbar', '0008_auto_20211202_0229'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_details', models.CharField(max_length=500)),
                ('reviewer_name', models.CharField(max_length=50)),
                ('reviewer_image', models.ImageField(upload_to='')),
            ],
        ),
    ]

# Generated by Django 3.2.9 on 2021-12-07 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navbar', '0011_alter_customer_review_reviewer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_review',
            name='reviewer_image',
            field=models.ImageField(upload_to=''),
        ),
    ]

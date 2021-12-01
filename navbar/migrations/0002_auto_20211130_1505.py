# Generated by Django 3.2.9 on 2021-11-30 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navbar', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='navbar_items',
            old_name='nav_title',
            new_name='navText',
        ),
        migrations.RemoveField(
            model_name='navbar_items',
            name='nav_link',
        ),
        migrations.AddField(
            model_name='navbar_items',
            name='link',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
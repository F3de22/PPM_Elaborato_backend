# Generated by Django 5.0.6 on 2024-06-17 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_rename_name_playlist_playlist_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='song',
            name='slug',
            field=models.SlugField(),
        ),
    ]
# Generated by Django 5.0.6 on 2024-06-19 13:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0010_rename_songs_p_playlist_songs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='image',
            field=models.ImageField(default='/images/music-placeholder.png', upload_to='playlist_images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])]),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='songs',
            field=models.ManyToManyField(related_name='playlist', to='music.song'),
        ),
    ]

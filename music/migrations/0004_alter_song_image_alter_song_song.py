# Generated by Django 5.0.6 on 2024-06-17 09:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_alter_playlist_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.ImageField(default='https://placehold.co/300x300/png', upload_to='songimage/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])]),
        ),
        migrations.AlterField(
            model_name='song',
            name='song',
            field=models.FileField(default='name', upload_to='songs/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav'])]),
        ),
    ]

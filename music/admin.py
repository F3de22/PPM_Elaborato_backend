from django.contrib import admin
from .models import Song, Playlist
# Register your models here:


class MusicAdmin(admin.ModelAdmin):
    list_display = ["name", "artist"]
    search_fields = ["name", "artist"]
    prepopulated_fields = {"slug": ("name",)}


class Meta:
    model = Song


admin.site.register(Song)
admin.site.register(Playlist)

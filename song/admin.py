from django.contrib import admin
from .models import Song
# Register your models here.


class SongAdmin(admin.ModelAdmin):
    list_display = ["__str__", "artist"]
    search_fields = ["name", "artist"]
    prepopulated_fields = {"slug": ("name",)}


class Meta:
    model = Song


admin.site.register(Song, SongAdmin)
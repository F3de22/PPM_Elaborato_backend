from django.contrib import admin
from .models import Song
# Register your models here:


class MusicAdmin(admin.ModelAdmin):
    list_display = ["name", "artist", "album"]
    search_fields = ["name", "artist", "album"]
    prepopulated_fields = {"slug": ("name",)}


class Meta:
    model = Song


admin.site.register(Song, MusicAdmin)

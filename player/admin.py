from django.contrib import admin
from .models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    fields = ('user', 'name', 'institute_id', 'contact',)
    list_display = fields
from django.contrib import admin
from .models import Task
from markdownx.admin import MarkdownxModelAdmin

@admin.register(Task)
class TaskAdmin(MarkdownxModelAdmin):
    fields = ('name', 'text', 'points', 'correct',)
    list_display = ('name', 'points', 'correct',)
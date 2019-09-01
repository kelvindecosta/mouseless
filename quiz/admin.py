from django.contrib import admin
from .models import Task, Card, Answer
from markdownx.admin import MarkdownxModelAdmin

@admin.register(Task)
class TaskAdmin(MarkdownxModelAdmin):
    fields = ('name', 'text', 'points', 'correct',)
    list_display = ('name', 'points', 'correct',)


@admin.register(Card)
class CardAdmin(MarkdownxModelAdmin):
    fields = ('user',)
    list_display = ('user', 'score', 'start', 'last_time')

@admin.register(Answer)
class AnswerAdmin(MarkdownxModelAdmin):
    fields = ('card', 'task', 'value',)
    list_display = ('card', 'task', 'value',)
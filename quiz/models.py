from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Task(models.Model):
    name = models.CharField(max_length=20)
    text = MarkdownxField()
    points = models.IntegerField()
    correct = models.CharField(max_length=20)

    @property
    def formatted_markdown(self):
        return markdownify(self.text)

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    value = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now=True)
from django.contrib.auth.models import User
from django.db import models
from django.db.models import F, Sum, Max
from django.urls import reverse
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from datetime import datetime

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


class Card(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    start = models.DateTimeField(auto_now_add=True, auto_now=False)

    @property
    def score(self):
        score = self.answer_set.filter(value=F('task__correct')).aggregate(score=Sum('task__points')).get('score')
        if score is None:
            score = 0
        return score

    @property
    def last_time(self):
        last_time = self.answer_set.filter(value=F('task__correct')).aggregate(last_time=Max('submit')).get('last_time')
        if last_time is None:
            return None
        
        return str(last_time - self.start)


class Answer(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    value = models.CharField(max_length=20)
    submit = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('card', 'task'),)
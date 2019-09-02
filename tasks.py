import os
import frontmatter
from django.contrib.auth.models import User
from quiz.models import Task

task_dir = './tasks'
for t in [frontmatter.load(f) for f in [os.path.join(task_dir, filename) for filename in os.listdir(task_dir)]]:
    task , _= Task.objects.get_or_create(text=t.content, **t)
    task.save()

# exec(open('tasks.py').read())
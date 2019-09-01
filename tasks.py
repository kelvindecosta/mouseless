import os
import frontmatter
from django.contrib.auth.models import User
from quiz.models import Task

task_dir = './tasks'
for t in [frontmatter.load(f) for f in [os.path.join(task_dir, filename) for filename in os.listdir(task_dir)]]:
    Task(text=t.content, **t).save()

# exec(open('tasks.py').read())
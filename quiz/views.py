from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView
)
from .forms import UserRegisterForm
from .models import Task


@login_required
def home(request):
    user = request.user
    if user.is_superuser or user.player_set.count() > 0:
        return render(request, 'quiz/home.html')
    else:
        messages.warning(request, f'Please enter the player details before attempting the challenge')
        return redirect('player-list')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account created successfully!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'quiz/register.html', {'form': form})

class TaskListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Task
    template_name = 'quiz/task_list.html'
    context_object_name = 'tasks'

    def test_func(self):
        check = self.request.user.is_superuser or self.request.user.player_set.count() > 0
        if not check:
            messages.warning(self.request, f'Please enter the player details before attempting the challenge')
        return check
    
    def handle_no_permission(self):
        return redirect('player-list')


class TaskDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Task

    def test_func(self):
        check = self.request.user.is_superuser or self.request.user.player_set.count() > 0
        if not check:
            messages.warning(self.request, f'Please enter the player details before attempting the challenge')
        return check
    
    def handle_no_permission(self):
        return redirect('player-list')
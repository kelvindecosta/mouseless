from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView
)
from .forms import UserRegisterForm, AnswerForm
from .models import Task, Card, Answer
from django.views.generic.edit import FormMixin


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.user.is_superuser:
            card, _ = Card.objects.get_or_create(user=self.request.user)
            context['card'] = card

        return context
    
    def get_queryset(self):
        return Task.objects.all().order_by('points')



class TaskDetailView(LoginRequiredMixin, UserPassesTestMixin, FormMixin, DetailView):
    model = Task
    form_class = AnswerForm

    def get_success_url(self):
        return reverse('task-detail', kwargs={'pk': self.object.id})

    def test_func(self):
        check = self.request.user.is_superuser or self.request.user.player_set.count() > 0
        if not check:
            messages.warning(self.request, f'Please enter the player details before attempting the challenge')
        return check
    
    def handle_no_permission(self):
        return redirect('player-list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        card = self.request.user.card
        answer , _ = Answer.objects.get_or_create(card=card, task=self.object)
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def get_context_data(self, **kwargs):
        context = super(TaskDetailView, self).get_context_data(**kwargs)
        card = self.request.user.card
        answer , _ = Answer.objects.get_or_create(card=card, task=self.object)
        context['form'] = AnswerForm(instance=answer)
        return context
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def form_valid(self, form):
        form.instance.save()
        return super(TaskDetailView, self).form_valid(form)

@login_required
def leaderboard(request):
    leaderboard = list(filter(lambda t: t.score > 0, Card.objects.all()))
    if len(leaderboard) > 0:
        leaderboard = sorted(leaderboard, key=lambda t: t.score)[::-1][:10]
        leaderboard = sorted(leaderboard, key=lambda t: t.last_time)
    context= {
        'leaderboard' : leaderboard
    }
    
    return render(request, 'quiz/leaderboard.html', context=context)

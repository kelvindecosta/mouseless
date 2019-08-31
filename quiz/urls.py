from django.urls import path
from .views import (
    TaskListView,
    TaskDetailView
)

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('<pk>/', TaskDetailView.as_view(), name='task-detail'),
]
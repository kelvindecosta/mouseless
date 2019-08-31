from django.urls import path
from .views import (
    PlayerListView,
    PlayerCreateView,
    PlayerUpdateView,
    PlayerDeleteView
)

urlpatterns = [
    path('', PlayerListView.as_view(), name='player-list'),
    path('new/', PlayerCreateView.as_view(), name='player-create'),
    path('<pk>/update/', PlayerUpdateView.as_view(), name='player-update'),
    path('<pk>/delete/', PlayerDeleteView.as_view(), name='player-delete'),
]
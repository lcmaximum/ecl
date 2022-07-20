from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('episodes/', views.episodes_index, name='episodes_index'),
    path('episodes/<int:episode_id>', views.episode_detail, name='detail'),
    path('episodes/create/', views.EpisodeCreate.as_view(), name='episode_create'),
    path('episodes/<int:pk>/update/', views.EpisodeUpdate.as_view(), name='episode_update'),
    path('episodes/<int:pk>/delete', views.EpisodeDelete.as_view(), name='episode_delete'),
    path('episodes/<int:episode_id>/add_review/', views.add_review, name='add_review'),
    path('profile/', views.user_profile, name='profile')
]
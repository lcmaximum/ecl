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
    path('profile/', views.user_profile, name='profile'),
    path('episodes/<int:episode_id>/assoc_char/<int:char_id>/', views.assoc_char, name='assoc_char'),
    path('episodes/<int:episode_id>/unassoc_char/<int:char_id>/', views.unassoc_char, name='unassoc_char'),

    path('characters/', views.CharList.as_view(), name='char_index'),
    path('characters/<int:pk>/', views.CharDetail.as_view(), name='char_detail'),
    path('characters/create/', views.CharCreate.as_view(), name='char_create'),
    path('characters/<int:pk>/update/', views.CharUpdate.as_view(), name='char_update'),
    path('characters/<int:pk>/delete/', views.CharDelete.as_view(), name='char_delete'),
]
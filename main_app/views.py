from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Episode
from .forms import ReviewForm



# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def episodes_index(request):
    episodes = Episode.objects.all()
    return render(request, 'episodes/index.html', {'episodes': episodes})

def episode_detail(request, episode_id):
    episode= Episode.objects.get(id=episode_id)
    review_form = ReviewForm()
    return render(request, 'episodes/detail.html',{'episode': episode, 'review_form': review_form})

def add_review(request, episode_id):
    form = ReviewForm(request.POST)
    new_review = form.save(commit=False)
    new_review.episode_id= episode_id
    new_review.user = request.user
    new_review.save()
    return redirect('detail', episode_id=episode_id)

def user_profile(request):
    return render(request, 'profile.html')


class EpisodeCreate(CreateView):
    model= Episode
    fields='__all__'

class EpisodeUpdate(UpdateView):
    model=Episode
    fields=['user_headline']

class EpisodeDelete(DeleteView):
    model=Episode
    success_url='/episodes/'

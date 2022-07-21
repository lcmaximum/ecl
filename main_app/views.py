from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Episode, Character
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
    char_ids = episode.characters.all().values_list('id')
    characters = Character.objects.exclude(id__in=char_ids)
    return render(request, 'episodes/detail.html',{'episode': episode, 'review_form': review_form, 'characters': characters})

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

class CharList(ListView):
  model = Character

class CharDetail(DetailView):
  model = Character

class CharCreate(CreateView):
  model = Character
  fields = '__all__'

class CharUpdate(UpdateView):
  model = Character
  fields = ['played_by', 'description']

class CharDelete(DeleteView):
  model = Character
  success_url = '/characters/'

def assoc_char(request, episode_id, char_id):
  episode = Episode.objects.get(id=episode_id)
  episode.characters.add(char_id)
  return redirect('detail', episode_id=episode_id)

def unassoc_char(request, episode_id, char_id):
  episode = Episode.objects.get(id=episode_id)
  episode.characters.remove(char_id)
  return redirect('detail', episode_id=episode_id)

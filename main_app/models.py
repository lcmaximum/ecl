from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Character(models.Model):
  name = models.CharField(max_length=50)
  played_by = models.CharField(max_length=50)
  description = models.CharField(max_length=75)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('char_detail', kwargs={'pk': self.id})


class Episode(models.Model):
    series_title = models.CharField(max_length=100)
    ep_title = models.CharField(max_length=150)
    ep_season = models.IntegerField()
    ep_number = models.IntegerField()
    user_headline = models.CharField(max_length=100)

    characters = models.ManyToManyField(Character)

    def __str__(self):
        return f'{self.ep_title} ({self.series_title})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'episode_id' : self.id})

class Review(models.Model):
    headline = models.CharField(max_length=100)
    content = models.TextField(max_length=500)

    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"Review {self.id} - {self.headline}"

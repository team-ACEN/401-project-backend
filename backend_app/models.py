from django.db import models
from django.urls import reverse

# Create your models here.

class Movie(models.Model):
  title = models.CharField(max_length=200)
  poster = models.URLField(max_length=200)
  services = models.TextField(blank=True)

  def get_absolute_url(self):
    return reverse('movie_detail', args=[str(self.id)])
  def __str__(self):
    return self.title


class Show(models.Model):
  title = models.CharField(max_length=200)
  poster = models.URLField(max_length=200)
  services = models.TextField(blank=True)

  def get_absolute_url(self):
    return reverse('show_detail', args=[str(self.id)])
  
  def __str__(self):
    return self.title

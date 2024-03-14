from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={"post_id": self.pk})
    class Meta:
        ordering = ['id']

class Comments(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments_article', to_field='id')
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='id')
    username = models.TextField(blank=True)
    content = models.TextField(blank=False)
    time_create = models.DateTimeField(auto_now_add=True)



    def get_absolute_url(self):
        return reverse('post', kwargs={"post_id": self.pk})
    class Meta:
        ordering = ['id']
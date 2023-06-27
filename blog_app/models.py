from django.conf import settings
from django.contrib.auth import get_user_model
import accounts
from accounts.models import CustomUser
from django.db import models
from django.urls import reverse

# Create your models here.

global primary_key

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author_id = CustomUser.id
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
    )
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        primary_key = str(self.pk)
        return reverse('blog_detail', args=[primary_key])
    class Meta:
        ordering = ('-date',)

class Comment(models.Model):
    blog = models.ForeignKey(
        Blog,
        on_delete = models.CASCADE,
        related_name = 'comments',
        )
    comment = models.CharField(max_length=140)
    comment_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
    )
    class Meta:
        ordering = ["comment_date"]

    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse('blog_detail', args=[primary_key])

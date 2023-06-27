import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile_image = models.CharField(max_length=500, null=True, blank=True)
    username = models.CharField(max_length=20, null=False, unique=True)
    name = models.CharField(max_length=30, null=False, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])

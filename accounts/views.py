from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

# Create your views here.


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home")
    template_name = "signup.html"


class ProfileView(LoginRequiredMixin, TemplateView):
    model = CustomUser
    template_name = "profile.html"
    login_url = "home"


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = "profile_edit.html"
    fields = ["profile_image", "username", "name", "age", "bio", "email"]
    login_url = "home"

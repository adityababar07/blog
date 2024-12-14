from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, TemplateView, UpdateView, DetailView
from django.shortcuts import get_object_or_404
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth.models import User

# Create your views here.


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'


class ProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'profile.html'
    login_url = 'home'
    context_object_name = 'profile'

    def get_object(self):
        # Fetch the user based on the username from the URL
        username = self.kwargs.get('username')
        return CustomUser.objects.get(username=username)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'profile_edit.html'
    fields = ['profile_image', 'username', 'name', 'age', 'bio', 'email']
    login_url = 'home'
    
    def get_success_url(self):
        # Optional, you can also use get_success_url if you prefer
        username = self.object.username
        return reverse_lazy('profile', kwargs={'username': username})

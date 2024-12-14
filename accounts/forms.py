from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('name', 'profile_image', 'username','email', 'age', 'bio')
        widgets = {
            'name': forms.TextInput(attrs={
                        'class':'form-control',
                        'placeholder':'Name',
                }),
            'username': forms.TextInput(attrs={
                        'class':'form-control',
                        'placeholder':'Username',
                }), 
            'email': forms.TextInput(attrs={
                        'class':'form-control',
                        'placeholder':'Email',
                }),
            'bio': forms.TextInput(attrs={
                        'class':'form-control',
                        'placeholder':'Bio',
                }),
            'profile_image': forms.TextInput(attrs={
                        'class':'form-control',
                        'placeholder':'Url of your profile',
                }),
            'age': forms.TextInput(attrs={
                        'class':'form-control',
                        'placeholder':'Age',
                }),

        }
        


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('name','profile_image', 'username','password', 'email', 'age', 'bio')
        widgets = {
            'name': forms.TextInput(attrs={
                        'class':'form-control',
                        'placeholder':'Name',
                }),
            'username': forms.TextInput(attrs={
                        'class':'form-control',
                        'placeholder':'Username',
                }), 
            'password': forms.TextInput(attrs={
                        'class':'form-control',
                        'placeholder':'Password',
                }),
        }
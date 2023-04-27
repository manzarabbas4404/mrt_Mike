from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from django import forms
from django.forms import widgets
from .models import *


class SignUpForm(UserCreationForm):
    username = forms.CharField(label=('Username'),max_length=150,help_text=('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'), error_messages={'unique': ("A user with that username already exists.")},widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=50, help_text='Required. Inform a valid email address.',
                             widget=(forms.TextInput(attrs={'class': 'form-control'})))
    password1 = forms.CharField(label=('Password'), widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label=('Password Confirmation'), widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                help_text=('Just Enter the same password, for confirmation'))
    
    class Meta:
        model= User
        fields = ('username', 'email', 'password1', 'password2')



class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'age', 'city', 'followers', 'following', 'profession']
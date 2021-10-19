from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='')
    last_name = forms.CharField(max_length=100, help_text='')
    email = forms.EmailField(max_length=150, help_text='')


    class Meta:
        model = User
        fields = ('username','password1', 'password2', 'first_name', 'last_name', 'email' )
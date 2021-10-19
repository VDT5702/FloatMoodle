# Create your views here.

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
import requests

def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('login')
    else:
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})

def showsome(request, userid):
    displaynames=User.objects.all()
    x = [0]+list(User.objects.all().values_list('username', flat=True))
    c = [0]+list(User.objects.all().values_list('first_name', flat=True))
    d = [0]+list(User.objects.all().values_list('last_name', flat=True))
    r = userid
    context1 = {'allusers':displaynames, 'username':x[r], 'first_name':c[r],'last_name':d[r]}
    return render(request,'profile.html', context1)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {'form': form})

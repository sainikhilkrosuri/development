from django.shortcuts import render, redirect
import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
@login_required(login_url='login')
def webhook(request):
    return render(request, 'webhook.html')

#@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

def register(request):
    form = create_account()
    if request.method == 'POST':
        register_user = create_account(request.POST)
        if register_user.is_valid():
            register_user.save()
            return redirect('login')
        else:
            form = create_account()
            return redirect('login')
    return render(request, 'register.html', {'form':form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        else:
            form = AuthenticationForm()
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')
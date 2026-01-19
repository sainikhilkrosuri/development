from django.shortcuts import render, redirect
import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from .forms import *

# Create your views here.

def webhook(request):
    if request.method == 'POST':
        return None
    return render(request, 'webhook.html')

def login(request):
    
    return render(request, 'login.html')

def logout(request):
    logout(request)
    return redirect('login')
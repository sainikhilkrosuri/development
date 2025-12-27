from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def webhook(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        return JsonResponse({'status': 'success', 'message': 'Payload received'})
    return render(request, 'webhook.html')
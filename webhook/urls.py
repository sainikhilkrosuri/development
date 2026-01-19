from django.urls import path
from .views import *

urlpatterns = [
    path('', webhook, name = 'webhook'),
    path('login/', login, name = 'login'),
    path('logout/', logout, name = 'logout'),
]
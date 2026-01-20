from django.urls import path
from .views import *

urlpatterns = [
    path('', webhook, name = 'webhook'),
    path('login/', login_user, name = 'login'),
    path('logout/', logout_user, name = 'logout'),
    path('register/', register, name = 'register'),
    path('index/', index, name = 'index'),
]
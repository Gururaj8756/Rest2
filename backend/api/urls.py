from urllib.parse import urlparse
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import api_home

urlpatterns = [
    path('auth/',obtain_auth_token),
    path('',api_home), #Local host:8000
    
]

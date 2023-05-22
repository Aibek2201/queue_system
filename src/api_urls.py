from django.contrib.auth import login
from django.urls import path, include

login



urlpatterns = [
    path('v1/', include('api_urls.v1')),
]


from django.urls import path, include

from users import views


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('auth/', views.auth, name='auth'),
]
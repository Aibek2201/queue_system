from django.urls import path, include


urlpatterns = [
    path('users/', include('users.urls.v1')),
    path('queues/', include(('queues.urls.v1', 'queues'), namespace='queues')),
]
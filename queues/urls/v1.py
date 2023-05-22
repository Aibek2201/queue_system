from django.urls import path

from queues import views


app_name = 'queues'

urlpatterns = [
    path('welcome/', views.welcome, name='home'),
    path('create/', views.queue_create, name='queue_create'),
    path('ticket/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
    path('queues/', views.queue_list, name='queue_list'),
    path('monitoring/', views.queue_monitoring, name='queue_monitoring'),
    path('accept/', views.accept, name='accept'),
    path('get_first_queue/', views.get_first_queue, name='get_first_queue'),
]
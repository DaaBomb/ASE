from django.urls import path
from notifs import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notifications/', views.allNotifications, name='notifications'),
]
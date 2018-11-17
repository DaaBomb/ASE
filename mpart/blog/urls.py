from django.conf.urls import url
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.details, name='details'),
    path('post/new/', views.newpost, name='newpost'),
    path('post/<int:pk>/edit', views.editpost, name='editpost'),
    path('post/<int:pk>/delete', views.deletepost, name='deletepost'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.addcomment, name='add-comment'),
]
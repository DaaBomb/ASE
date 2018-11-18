from django.conf.urls import url
from history import views

urlpatterns = [
 url(r'^$',views.trials,name = 'trials'),
]

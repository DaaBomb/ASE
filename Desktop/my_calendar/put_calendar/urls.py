from django.urls import path
from put_calendar import views

urlpatterns = [
  path('next/',views.date,name = "date"),
  path('back/',views.date1,name = "date1"),
]

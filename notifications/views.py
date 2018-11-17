from django.shortcuts import render, redirect
from .models import NotificationList

# Create your views here.
def index(request):
    latest = NotificationList.objects.last()
    all_notifications = NotificationList.objects.all()
    all_notifications.reverse()
    rev_all = list(reversed(all_notifications))
    context = {'latest':latest,
               'rev_all':rev_all}
    return render(request,'notifications/index.html',context)

def update(request,notify_id):
    item = NotificationList.objects.get(pk = notify_id)
    item.read = True
    item.save()
    return redirect('notifications:index')

from django.shortcuts import render
from notifs.models import Webpage

# Create your views here.
def index(request):
    webpage = Webpage.objects.all()
    record_dict = {'pages': webpage}
    return render(request, 'notifs/ceo.html', context=record_dict)

def allNotifications(request):
    webpage = Webpage.objects.all()
    record_dict = {'pages':webpage}
    return render(request, 'notifs/allNotifications.html', context=record_dict)
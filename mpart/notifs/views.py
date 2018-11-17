from django.shortcuts import render
from notifs.models import Webpage

# Create your views here.
def home(request):
    return render(request, "notifs/index.html")

def index(request):
    webpage = Webpage.objects.all()
    record_dict = {'pages': webpage}
    return render(request, 'notifs/ceo.html', context=record_dict)

def allNotifications(request):
    webpage = Webpage.objects.all()
    record_dict = {'pages':webpage}
    return render(request, 'notifs/allNotifications.html', context=record_dict)

def ceohome(request):
    return render(request, 'notifs/ceo.html')
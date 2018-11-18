from django.shortcuts import render

from history.models import recent_activity
# Create your views here.
def index(request):
    return render(request , 'history/index.html')
def trials(request):
    last_task = recent_activity.objects.order_by('-dates')
    task_dict = {"trials": last_task}
    return render(request,'history/users.html',context=task_dict)

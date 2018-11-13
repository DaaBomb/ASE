import post as post
from django.utils import timezone
from django.shortcuts import render
from blog.models import post
# Create your views here.

def index(request):
    posts_dict={'posts':post.objects.order_by('-timestamp')}
    return render(request, 'blog/index.html', context=posts_dict)

def details(request, pk):
    posts_dict={'posts':post.objects.filter(id=pk)}
    return render(request, 'blog/details.html', context=posts_dict)
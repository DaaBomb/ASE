from django.shortcuts import render
from blog.models import post
# Create your views here.

def index(request):
    posts_dict={'posts':post.objects.all()}
    return render(request, 'blog/index.html', context=posts_dict)
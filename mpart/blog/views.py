import post as post
from django.http import Http404
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from blog.models import post, comment
from .forms import postform, commentform
from django.shortcuts import redirect


# Create your views here.

def index(request):
    pindex = post.objects.order_by('-timestamp')
    posts_dict_index = {'posts': pindex}

    return render(request, 'blog/index.html', posts_dict_index)


def details(request, pk):
    posts = get_object_or_404(post,id=pk)
    comments = comment.objects.filter(post=posts)
    posts_dict_details = {'posts':posts, 'allcomments': comments}
    return render(request, 'blog/details.html', posts_dict_details)


def newpost(request):
    if request.method == "POST":
        newform = postform(request.POST)
        if newform.is_valid():
            new_post = newform.save(commit=False)
            new_post.author = request.user
            new_post.published_date = timezone.now()
            new_post.save()
            return redirect('index')
    else:
        newform = postform()
    return render(request, 'blog/newpost.html', {'form': newform})


def editpost(request, pk):
    posts = get_object_or_404(post, pk=pk)
    if posts.author != request.user:
        raise Http404()

    if request.method == "POST":
        editform = postform(request.POST, instance=posts)
        if editform.is_valid():
            edit_post = editform.save(commit=False)
            edit_post.published_date = timezone.now()
            edit_post.save()
            return redirect('index')

    else:
        editform = postform(instance=posts)
        return render(request, 'blog/editpost.html', {'form': editform})


def deletepost(request, pk):
    posts = get_object_or_404(post, pk=pk)
    if posts.author != request.user:
        raise Http404()

    posts.delete()
    return redirect('index')

def addcomment(request, pk):
    posts = get_object_or_404(post,pk=pk)
    if request.method == 'POST':
        com_form=commentform(request.POST)
        if com_form.is_valid():
            comment_var =com_form.save(commit=False)
            comment_var.post=posts
            comment_var.save()
            return redirect('index')
    else:
        com_form = commentform()
    return render(request, 'blog/addcomment.html',{'form':com_form})
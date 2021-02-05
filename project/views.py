from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm


def index(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    return render(request, 'Home.html', {'posts': posts,
                                         'comments': comments})


def FormPost(request):
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
        else:
            error = 'данные введены некорректно'
    form = PostForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'AddPost.html', data)

def FormCommens(request):
    error = ''
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
        else:
            error = 'данные введены некорректно'
    form = CommentForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'addComments.html', data)
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Post, Comment
from .forms import PostForm, CommentForm


def index(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    return render(request, 'Home.html', {'posts': posts,
                                         'comments': comments})


def FormPost(request):
    posts = Post.objects.all()
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_comments')
        else:
            error = 'данные введены некорректно'
    form = PostForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'AddPost.html', data)


def FormComments(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    comment = Comment.objects.filter(commented_post=posts)
    error = ''
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.user = request.user
            comment.posts = posts
            comment.save()
            return redirect('/')
    else:
        error = 'данные введены некорректно'
    form = CommentForm()
    data = {
        'form': form,
        'error': error,
        'comment': comment,
        'posts': posts,
        'comments': comments,
    }
    return render(request, 'Home.html', data)

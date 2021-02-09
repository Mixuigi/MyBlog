from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.utils import timezone
from django.contrib.auth import authenticate, login
from .models import *
from .forms import *


def Registration(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return HttpResponse('Authenticated successfully')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def FormPost(request):
    posts = Post.objects.all()
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home_Page')
        else:
            error = 'данные введены некорректно'
    form = PostForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'AddPost.html', data)


def Home(request):
    user = User.objects.all()
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
        'user': user,
    }
    return render(request, 'Home.html', data)

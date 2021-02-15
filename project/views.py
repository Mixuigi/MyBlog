from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import authenticate, login
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
    posts = Post.objects.filter(status='published')
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save()
            new_post.user = request.user
            new_post.save()
            return redirect('Home_Page')
        else:
            error = 'данные введены некорректно'
    form = PostForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'AddPost.html', data)


def objects():
    user = User.objects.all()
    posts = Post.objects.filter(status='published', )
    comments = Comment.objects.all()
    comment = Comment.objects.filter(commented_post=posts, )
    return user, posts, comments, comment


def Home(request):
    user, posts, comments, comment = objects()
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


def AddComment(request, POST):
    post = get_object_or_404(Post, slug=POST,
                             status='published')
    user, posts, comments, comment = objects()
    error = ''
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save()
            new_comment.commented_post = post
            new_comment.user = request.user
            new_comment.save()


            return redirect('/')
    else:
        error = 'данные введены некорректно'
    form = CommentForm()
    data = {'post': post,
            'posts': posts,
            'comments': comments,
            'form': form,
            'error': error, }
    return render(request, 'Post.html', data)

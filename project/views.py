from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Comment
from .forms import PostForm
from django.utils import timezone


def index(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    return render(request, 'index.html', {'posts': posts,
                                          'comments': comments})


def FormPost(request):
    postform = PostForm()
    return render(request, 'FormHead.html', {'postform': postform})

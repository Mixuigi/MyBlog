from django.shortcuts import render, redirect, get_object_or_404, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views import generic

from .forms import *
from django.contrib.auth.forms import UserCreationForm


def Authentication(request):
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


class RegistrationForm(UserCreationForm):
    # first_name = forms.CharField(
    #   required=False,
    #  label='First Name'
    # )

    class Meta(UserCreationForm.Meta):
        fields = (*UserCreationForm.Meta.fields,)  # 'first_name')


class SignUpView(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('Home_Page')
    template_name = 'Register.html'


def FormPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save()
            new_post.user = request.user
            new_post.save()
            return redirect('Home_Page')
    form = PostForm()
    data = {
        'form': form,
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
    data = {
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
    data = {'post': post,
            'posts': posts,
            'comments': comments, }
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save()
            new_comment.commented_post = post  # присваивание комменту slug поста
            new_comment.user = request.user  # присваивание комменту юзера
            new_comment.save()
            return render(request, 'Post.html', data)
    form = CommentForm()
    data = {'post': post,
            'posts': posts,
            'comments': comments,
            'form': form,
            }
    return render(request, 'Post.html', data)

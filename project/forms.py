from django import forms
from django.forms import ModelForm, TextInput, Textarea
from .models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['slug', 'text_post']

        widgets = {
            'slug': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'название/тема поста'
            }),
            'text_post': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'текст поста'
            }),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['commented_post', 'text_comment', 'user']

        widgets = {
            'text_comment': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'комментарий'
            }),
        }

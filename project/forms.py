from django import forms
from django.utils import timezone


class PostForm(forms.Form):
    slug = forms.CharField(max_length=20, label='тема поста')
    text_post = forms.CharField(max_length=1000, widget=forms.Textarea, label='текст')
    createdtime = forms.DateTimeField()



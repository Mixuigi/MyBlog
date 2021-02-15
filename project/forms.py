from django import forms
from django.forms import ModelForm, TextInput, Textarea
from .models import Post, Comment, User


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


'''class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [ 'text_comment', 'user']

        widgets = {
            'text_comment': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'комментарий'
            }),

        }'''

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text_comment', )
#f = CommentForm(initial={'commented_post': 'commented_post'})


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

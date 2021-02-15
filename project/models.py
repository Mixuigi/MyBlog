from django.db import models
from django.contrib.auth.models import User
# from django.utils import timezone
from django.conf import settings
from django.urls import reverse


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True, null=True, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=30)
    text_post = models.TextField(max_length=1000)
    post_date_published = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ('-post_date_published',)

    def get_absolute_url(self):
        return reverse('project:add_comment', args=[self.slug])


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    commented_post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    text_comment = models.TextField(max_length=1000)
    comment_date_published = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        ordering = ('comment_date_published',)

    def __str__(self):
        return f' {self.text_comment} by {self.user} on {self.commented_post}'
       # return self.text_comment



    # def com_was_published_recently(self):
    # self.comment_date_published = timezone.now()
    # self.save()

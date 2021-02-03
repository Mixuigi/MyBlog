from django.db import models
from django.utils import timezone
from django.conf import settings
import datetime


class Post(models.Model):
    slug = models.CharField(max_length=30)
    text_post = models.TextField(max_length=1000)
    post_date_published = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.slug

    def was_published_recently(self):
        self.post_date_published = timezone.now()
        self.save()


class Comment(models.Model):
    commented_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text_comment = models.TextField(max_length=1000)
    comment_date_published = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.text_comment

    def com_was_published_recently(self):
        self.comment_date_published = timezone.now()
        self.save()

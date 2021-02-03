from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('slug', 'post_date_published', 'text_post')
    list_filter = ('post_date_published',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('commented_post', 'comment_date_published', 'text_comment')
    list_filter = ('comment_date_published',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

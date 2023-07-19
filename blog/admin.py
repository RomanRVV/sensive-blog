from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'published_at')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    raw_id_fields = ['likes']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title']

from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


"""
Create the post/recipe for admin pannel
"""
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')


"""
 Create the comment section for admin pannel
"""
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    """
    Create the function for approving the comments from the admin
    """
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
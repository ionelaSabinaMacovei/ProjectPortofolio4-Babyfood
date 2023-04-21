from django.contrib import admin
from .models import Post, Comment, Category, Profile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Add field for recipe/post in admin panel
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Add field for comment in admin panel
    """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    """
    Create the function for approving the comments from the admin
    """
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    """
    Add field for category in admin panel
    """
    list_display = ('cat_title',)
    search_fields = ['cat_title']
    prepopulated_fields = {'slug': ('cat_title',)}


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Add field for the profile in the admin panel
    """
    list_display = ('user',)
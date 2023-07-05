from .models import Comment, Profile, Post
from django.contrib.auth.models import User
from django import forms


class CommentForm(forms.ModelForm):
    """
    Form for post comments
    """
    class Meta:
        model = Comment
        fields = ['body', 'parent']

        widgets = {
            'body': forms.TextInput(),
        }


class UserUpdateForm(forms.ModelForm):
    """
    Form for profile name update
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """
    Form for profile image update
    """
    class Meta:
        model = Profile
        fields = ['image', ]


class PostForm(forms.ModelForm):
    """
    All details of the post form
    """
    class Meta:
        model = Post
        exclude = ('author', 'slug',
                   'likes', 'updated_on',
                   'excerpt', 'status',)


class PostSearchForm(forms.Form):
    q = forms.CharField()
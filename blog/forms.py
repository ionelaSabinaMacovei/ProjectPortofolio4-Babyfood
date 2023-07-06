from .models import Comment, Profile, Post, Reply
from django.contrib.auth.models import User
from django import forms


class CommentForm(forms.ModelForm):
    """
    Form for post comments
    """
    class Meta:
        model = Comment
        fields = ('body',)

        labels = {"body": "Comment:"}

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 70, 'placeholder': "Enter Your Comment"}),
        }


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('reply_body',)

        widgets = {
            'reply_body': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'cols': 10}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ReplyForm, self).__init__(*args, **kwargs)


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
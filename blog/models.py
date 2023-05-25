from django.db import models
import uuid
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse

STATUS = ((0, "Draft"), (1, "Published"))
User = get_user_model()


class Profile(models.Model):
    """
    Model for user profile
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    image = CloudinaryField('image')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'{self.user.username} Profile'


class Category(models.Model):
    """
    Category Model linked to each post
    """
    cat_title = models.CharField(max_length=80, blank=False)
    cat_featured_image = CloudinaryField('image', default='placeholder')
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.cat_title
    

class Post(models.Model):
    """
    Model for recipe
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    ingredients = models.TextField()
    method = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name="categories")

    class Meta:
        """ Ordering class """
        ordering = ["-created_on"]

    def __str__(self):
        """ Return title """
        return self.title

    def number_of_likes(self):
        """ Return amount of likes """
        return self.likes.count()


class Comment(models.Model):
    """
    Comment Model
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

    def get_absolute_url(self):
        """Sets absolute URL"""
        return reverse('post_detail', args=[self.post.slug])



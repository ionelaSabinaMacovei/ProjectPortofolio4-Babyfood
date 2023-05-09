from . import views

from django.conf.urls import url

from django.urls import path, include

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/', views.about, name="about"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('add_post', views.add_post, name='add_post'),
    path('search/', views.post_search, name="post_search"),
    path('profile/<slug:slug>', views.profile_view, name='profile'),
    path('edit/<slug:slug>/', views.edit_post, name='edit_post'),
    path('delete/<slug:slug>/', views.delete_post, name='delete_post'),
    path('<int:pk>/delete_comment',
         views.delete_comment, name='delete_comment'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('category/<category>/', views.CategoryList.as_view(), name='category'),
]


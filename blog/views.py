from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from .models import Post, Comment, Category, Profile
from .forms import CommentForm, PostForm, PostSearchForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.text import slugify
from django.views.generic import UpdateView


def about(request):
    """
    Renders the about page
    """
    return render(request, 'about.html')


class PostList(generic.ListView):
    """
    For displaying current post
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('created_on')
    template_name = 'index.html'
    paginate_by = 8


class PostDetail(View):
    """
    For displaying selected post's detail
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('created_on')
        category = post.category
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "category": category,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Post method to add comments and likes
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        comments = post.comments.order_by('created_on')
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()
           
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": comment_form,
            },
        )


class PostLike(View):
    """
    For managing the like an unlike actions
    """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            messages.success(request, 'You have unliked this post.')
        else:
            post.likes.add(request.user)
            messages.success(request, 'You have liked this post, thanks!')

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def add_post(request):
    """ Add a post to the blog """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            form.save()
            messages.success(request, 'Successfully added post for review.')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to add post. \
                           Please ensure the form is valid.')
    else:
        form = PostForm()

    template = 'add_post.html',
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_post(request, slug):

    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST, request.FILES, instance=post)
    if request.user.id == post.author.id:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.slug = slugify(post.title)
                post.status = 1
                form.save()
                messages.success(request, 'Successfully updated post!')
                return redirect(reverse('home'))
            else:
                messages.error(request, 'Failed to update post. \
                    Please ensure the form is valid.')
        else:
            form = PostForm(instance=post)
    else:
        messages.error(request, 'Sorry. \
                    You are not authorised to perform that operaiton.')

    template = 'edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


@login_required
def delete_post(request, slug):
    """ Delete a post from the blog """

    post = get_object_or_404(Post, slug=slug)
    if request.user.id == post.author.id:
        post.delete()
        messages.success(request, 'Post deleted!')
        return redirect(reverse('home'))
    else:
        messages.error(request, 'Sorry. \
            You are not authorised to perform that operaiton.')


class CatListView(generic.ListView):
    """
    For displaying categories
    """
    template_name = 'category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__cat_title=self.kwargs['category']).filter(status=1)
        }
        return content


def category_list(request):
    """ Return a list of categories for the dropdown in the menu """
    category_list = Category.objects.all()
    context = {
        "category_list": category_list,
    }
    return context


def post_search(request):
    """ Return a list of posts from a search term in the menu """
    form = PostSearchForm()
    q = ''
    results = []

    if 'q' in request.GET:
        form = PostSearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']
            results = Post.objects.filter(Q
                                          (title__icontains=q)
                                          | Q(method__icontains=q)).filter(status=1)

    return render(request, 'search.html', {
        'form': form,
        'q': q,
        'results': results
    })


@login_required
def delete_comment(request, pk):
    """ Delete a comment in the blog
    """
    Comment.objects.get(pk=pk).delete()
    messages.success(request, 'The comment was deleted successfully!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class edit_comment(SuccessMessageMixin, UpdateView):
    """
    Edit comment
    """
    model = Comment
    template_name = 'edit_comment.html'
    form_class = CommentForm
    success_message = 'The comment was successfully updated'


@login_required
def profile_view(request):
    """
    Renders the profile page
    """
    queryset = Post.objects.filter(author=request.user).order_by('created_on')
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'queryset': queryset,
    }
    return render(request, 'profile.html', context)


@login_required(login_url='sign_in')
def delete_account(request):
    profile = request.user.profile
    if request.method == 'POST':
        profile.delete()
        messages.success(request, 'Account Deleted!')
        return redirect('home')
    return render(request, 'delete_user.html')


from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView, TemplateView, DeleteView
from .models import Blog, Comment, Likes
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
from .forms import CommentForm
from django.contrib import messages
from functools import wraps


class MyBlogs(LoginRequiredMixin, TemplateView):
    template_name = 'Blog_API/my_blogs.html'

class EditBlog(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ('blog_title', 'blog_content', 'blog_image')
    template_name = 'Blog_API/edit_blog.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('Blog_API:blog_details', kwargs={'slug':self.object.slug,})

class BlogList(ListView):
    context_object_name = 'blogs'
    model = Blog
    template_name = 'Blog_API/blog_list.html'

class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'Blog_API/create_blog.html'
    fields = ('blog_title', 'blog_content', 'blog_image')

    def form_valid(self,form):
        blog_object = form.save(commit=False)
        blog_object.author = self.request.user
        title = blog_object.blog_title
        blog_object.slug = title.replace(' ','-') + '-' + str(uuid.uuid4())
        blog_object.save()
        return HttpResponseRedirect(reverse('index'))


def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    comment_form = CommentForm()
    already_liked = Likes.objects.filter(blog=blog, user=request.user)
    if already_liked:
        liked = True
    else:
        liked = False

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse('Blog_API:blog_details', kwargs={'slug':slug}))
    return render(request, 'Blog_API/blog_details.html', context={'blog':blog, 'comment_form':comment_form, 'liked':liked})


@login_required
def like(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Likes.objects.filter(blog=blog, user=user)
    if not already_liked:
        liked_blog = Likes(blog=blog, user=user)
        liked_blog.save()
    return HttpResponseRedirect(reverse('Blog_API:blog_details', kwargs={'slug':blog.slug}))

@login_required
def dislike(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Likes.objects.filter(blog=blog, user=user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('Blog_API:blog_details', kwargs={'slug':blog.slug}))


# def profile_required(view):
#     @wraps(view)
#     def inner(request, *args, **kwargs) :
#         if request.user.is_authenticated():
#             return HttpResponseRedirect('/')
#         else:
#             return HttpResponse('Error Message')
#     return inner

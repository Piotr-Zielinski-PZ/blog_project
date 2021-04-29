from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    blog_title = models.CharField(max_length=256,verbose_name='Enter blog title')
    slug = models.SlugField(max_length=256, unique=True)
    blog_content = models.TextField(verbose_name='Enter your content')
    blog_image = models.ImageField(upload_to='blog_images', verbose_name='Place for image')
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.blog_title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-comment_date']

    def __str__(self):
        return self.blog_title

class Likes(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='liked_blog')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_author')

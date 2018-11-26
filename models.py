# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify
from django.utils.timezone import datetime
from datetime import datetime
from django.conf import settings

class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'tags'

    def __unicode__(self):
        return self.name

# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    published = models.BooleanField(default=0)
    body = models.TextField()
    published_at = models.DateTimeField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    tags = models.ManyToManyField(Tag,db_table='blog_tag')

    def __unicode__(self):
        return self.title

    @staticmethod
    def latest_posts(num_posts):
        today = datetime.today()
        blogs = Blog.objects.filter(published_at__lte=today).order_by('-updated_at')[:num_posts]
        return blogs

    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save()

    def comments(self):
        comment_set = Comment.objects.filter(blog=self).filter(parent_comment=None)
        return comment_set

    def is_published(self):
        if not self.published:
            return False
        return datetime.now(self.published_at.tzinfo) > self.published_at

    class Meta:
        db_table = 'blogs'
        get_latest_by = "updated_at"
        ordering = ['-updated_at']

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.body

    def children(self):
        child_comments = Comment.objects.filter(parent_comment=self)
        return child_comments

    class Meta:
        db_table = 'blogcomments'
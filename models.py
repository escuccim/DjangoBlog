# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.timezone import datetime

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    published = models.BooleanField(default=0)
    body = models.TextField()
    published_at = models.DateTimeField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.CharField(max_length=100, null=True, blank=True)
    image_width = models.IntegerField(null=True, blank=True)
    image_height = models.IntegerField(null=True, blank=True)
    tags = models.ManyToManyField(Tag)

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
        comment_set = Comment.objects.filter(blog=self).filter(parent=None)
        return comment_set

    class Meta:
        get_latest_by = "updated_at"
        ordering = ['-updated_at']

class Comment(models.Model):
    author = models.ForeignKey(User)
    body = models.TextField()
    blog = models.ForeignKey(Blog)
    parent = models.ForeignKey("self", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.body

    def children(self):
        child_comments = Comment.objects.filter(parent=self)
        return child_comments

    class Meta:
        pass
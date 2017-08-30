# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Blog, Tag, Author, Comment

# Register your models here.
admin.site.register(Blog)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Comment)
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Blog, Tag, Comment
from .forms import CommentForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def Index(request):
    all_blogs = Blog.objects.all()
    paginator = Paginator(all_blogs, 5)
    page = request.GET.get('page', 1)
    archives = get_archives()
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', {'blogs' : blogs, 'archives' : archives})

def Show(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    comment_form = CommentForm()
    user = request.user
    return render(request, 'blog/detail.html', {'blog' : blog, 'comment_form' : comment_form, 'user': user})

def Label(request, name):
    tag = get_object_or_404(Tag, name=name)
    blogs = Blog.objects.filter(tags=tag)

    return render(request, 'blog/index.html', {'blogs': blogs})

def PostComment(request, slug):
    blog = get_object_or_404(Blog, slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            if form.cleaned_data['parent_id']:
                parent = Comment.objects.get(pk=form.cleaned_data['parent_id'])
                comment.parent = parent
            comment.blog = blog
            author = Author.objects.get(user=request.user)
            comment.author = author
            comment.save()
        else:
            return HttpResponse("Invalid!")
            print form.errors
    else:
        pass

    return redirect('blog:show', slug=blog.slug)

def DeleteComment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    blog = comment.blog
    comment.delete()
    return redirect('blog:show', blog.slug)

def get_archives():
    blog_list = Blog.objects.raw("SELECT strftime('%m', updated_at) as month, strftime('%Y', updated_at) as year, id, slug, title from blog_blog order by year desc, month desc")
    blog_dict = {}
    month_dict = {}
    for item in blog_list:
        month_dict.setdefault(item.month, []).append([item.id, item.slug, item.title])
        blog_dict.setdefault(item.year, month_dict )

    return blog_dict

def Amp(request, slug):
    pass
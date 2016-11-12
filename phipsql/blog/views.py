from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Posts

def index(request):
    posts_list = Posts.objects.order_by('post_date')[:5]
    return render(request, 'blog/index.html', {'posts_list' : posts_list})

def detail(request, posts_id):
    post = get_object_or_404(Posts, pk = posts_id)
    return render(request, 'blog/posts.html', {'post': post})

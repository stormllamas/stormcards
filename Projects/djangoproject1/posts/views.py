from .models import Posts
from django.shortcuts import render
# from django.http import HttpResponse
#to get Posts from models.py into this file to posts/url

# Create your views here.
def index(request):
    # return HttpResponse('HELLO FROM POSTS')

    # brings in Posts from models.py
    posts = Posts.objects.all()[:10]

    context = {
        'title': 'Latest Posts',
        'posts': posts
    }

    return render(request, 'posts/index.html', context)

def details(request, id):
    post = Posts.objects.get(id=id)

    context = {
        'post': post
    }

    return render(request, 'posts/details.html', context)
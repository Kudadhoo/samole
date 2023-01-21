from django.shortcuts import render

from .models import Post,Likes
from django.urls import reverse
from django.http import HttpResponseRedirect


def projects(request):
    post = Post.objects.all()
    return render(request, 'home.html', {'post': post})


def detail(request, pk):
    dp = Post.objects.get(id=pk)


    return render(request, 'detail.html', {'dp': dp})


def like(request, pk):
    user = request.user
    post = Post.objects.get(id=pk)
    current_likes = post.likes
    liked = Likes.objects.filter(user=user, post=post).count()

    if not liked:
        Likes.objects.create(user=user, post=post)
        current_likes = current_likes + 1

    else:
        Likes.objects.filter(user=user, post=post).delete()
        current_likes = current_likes - 1
    post.likes = current_likes

    post.save()
    return HttpResponseRedirect(reverse('details', args=[pk]))

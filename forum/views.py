from django.db.models import Q
from django.shortcuts import render

from forum.models import *


def posts(request):
    """Страница со списком постов."""
    posts = Post.objects.all()
    if request.method == 'POST':
        search_string = request.POST['search_string']
        posts = posts.filter(Q(user__name__icontains=search_string) | Q(title__icontains=search_string) | Q(body__icontains=search_string))

    return render(request, 'forum/posts.html', {'posts': posts})

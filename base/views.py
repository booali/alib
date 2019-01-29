from django.shortcuts import render
from django.core.paginator import Paginator
from base.models import Post
#from django.http import HttpResponse


def index(request):
    kolohom = Post.objects.all()
    ss = {'as' : kolohom}
    return render(request, 'index.html', context=ss)

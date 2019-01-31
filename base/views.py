from django.shortcuts import render
from django.core.paginator import Paginator
from base.models import Post
#from django.http import HttpResponse


def index(request):
    kolohom = list(Post.objects.all())
    posts = Paginator(kolohom,3)
    
    page = request.GET.get('page')
    post = posts.get_page(page)
    ass = request.GET.get('ass')
    ss = {'as' : kolohom,'posts':post,'fun':ass}
    return render(request, 'index.html', context=ss)

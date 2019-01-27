from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    dict_aa = {}
    return render(request,'index.html',context=dict_aa)

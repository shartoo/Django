# -*- coding:utf-8 -*-

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from models import Article

def hello(request):
    return HttpResponse("Hello world!")

def home(request):
    post_list = Article.objects.all()  # 获取全部的Article对象
    return render(request, 'home.html', {'post_list': post_list})

def detail(request, my_args):
    post = Article.objects.all()[int(my_args)]
    str = ("title = %s, category = %s, date_time = %s, content = %s"
        % (post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)
'
def test(request) :
    return render(request,'test.html', {'current_time': datetime.now()})
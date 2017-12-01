# coding:utf-8
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

# 定义视图函数，作用是向前端返回数据
# 一般是前端通过urls.py中配置路由访问views.py中定义视图函数


def index(request):
    # 当通过路由访问时，返回一个字符串
    return HttpResponse(u'Djdango首页页面')

# 后台如何渲染html模板
def load_html(request):
    # return render(request, 'index.html', {'title':'后台传递首页', 'content':'Django后台返回的数据！'})
    # list_test = ['HTML', 'CSS', 'JS', 'FLASK', 'DJANGO']
    # return render(request, 'index.html', {'courses':list_test})
    # 向前端传字典数据
    info_dict = {'name':'张三', 'age':50}
    return render(request, 'index.html',{'info_dict':info_dict})
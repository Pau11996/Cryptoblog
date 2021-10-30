from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def news(request):
    catnew = NewsCategory.objects.all()
    news = News.objects.all()
    print(news)                                                     # I chek data in terminal
    return render(request, 'news/news.html', {'news': news, 'catnew': catnew})

def category(request, cat_id):
    new = News.objects.filter(cat_id=cat_id)
    catnew = NewsCategory.objects.all()
    return render(request, 'news/detail.html', {'cat_selected': cat_id, 'new': new, 'catnew': catnew})


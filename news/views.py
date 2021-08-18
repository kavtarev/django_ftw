from django.shortcuts import render
from django.http import HttpResponse
from .models import News_model


# Create your views here.

def index(request): # called action
    news = News_model.objects.all()
  
    return render(request,'news/index.html',{'news':news,'title':'news list'})

def test(request):
    return HttpResponse('<h1>Test page</h1>')
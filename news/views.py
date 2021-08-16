from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    print(request)
    return HttpResponse('hi pes')

def test(request):
    return HttpResponse('<h1>Test page</h1>')
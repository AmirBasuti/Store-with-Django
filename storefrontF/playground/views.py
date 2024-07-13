from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def say_hello(request):
    x = 1
    y = 2
    tmp = loader.get_template('hello.html')
    return HttpResponse(tmp.render())

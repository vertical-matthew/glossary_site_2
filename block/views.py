from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about(request):
    return HttpResponse('This is our about page')


def home(request):
    return HttpResponse('This is our home page')

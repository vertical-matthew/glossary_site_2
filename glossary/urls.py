from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

from block.views import about, home

def about(request):
    return HttpResponse('This is our about page')


def home(request):
    return HttpResponse('This is our home page')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about),
    path('', home),

]

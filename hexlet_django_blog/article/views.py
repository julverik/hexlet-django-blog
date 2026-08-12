from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
    context = {
        'app_name': 'Статьи',
    }
    return render(request, 'articles/index.html', context)

def about(request):
    return HttpResponse("about")
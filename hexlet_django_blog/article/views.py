from django.shortcuts import render
from django.views import View

class IndexView(View):
    def get(self, request):
        context = {
            'app_name': 'Статьи',
        }
        return render(request, 'articles/index.html', context)
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class IndexView(View):
    def get(self, request, tags=None, article_id=None):
        if tags is not None and article_id is not None:
            return HttpResponse(f"Статья номер {article_id}. Тег {tags}")
        
        context = {
            'app_name': 'Статьи',
        }
        return render(request, 'articles/index.html', context)
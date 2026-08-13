from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.urls import reverse

class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        return redirect(reverse('article', kwargs={'tags': 'python', 'article_id': 42}))


class AboutView(TemplateView):
    template_name = 'about.html'
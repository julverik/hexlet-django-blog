from django.urls import include, path
from hexlet_django_blog.views import IndexView, AboutView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('articles/', include('hexlet_django_blog.article.urls')),
]
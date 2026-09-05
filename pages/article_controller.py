from django.shortcuts import render

from .models import Article


class ArticleController:

    @staticmethod
    def index(request):
        articles = Article.objects.all().order_by('-published_at')

        return render(request, 'articles/index.html', {
            'articles': articles
        })
        
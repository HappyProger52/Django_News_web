from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ArticleForm
from .models import Article


class ArticleController:

    @staticmethod
    def index(request):
        articles = Article.objects.all().order_by('-published_at')

        paginator = Paginator(articles, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'articles/index.html', {
            'page_obj': page_obj
        })

    @staticmethod
    def show(request, article_id):
        article = get_object_or_404(Article, id=article_id)

        return render(request, 'articles/show.html', {
            'article': article
        })

    @staticmethod
    def create(request):
        form = ArticleForm()

        return render(request, 'articles/create.html', {
            'form': form
        })

    @staticmethod
    def store(request):
        form = ArticleForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('articles')

        return render(request, 'articles/create.html', {
            'form': form
        })

    @staticmethod
    def edit(request, article_id):
        article = get_object_or_404(Article, id=article_id)
        form = ArticleForm(instance=article)

        return render(request, 'articles/edit.html', {
            'form': form,
            'article': article
        })

    @staticmethod
    def update(request, article_id):
        article = get_object_or_404(Article, id=article_id)
        form = ArticleForm(request.POST, instance=article)

        if form.is_valid():
            form.save()
            return redirect('article_show', article_id=article.id)

        return render(request, 'articles/edit.html', {
            'form': form,
            'article': article
        })

    @staticmethod
    def delete(request, article_id):
        article = get_object_or_404(Article, id=article_id)

        if request.method == 'POST':
            article.delete()
            return redirect('articles')

        return render(request, 'articles/delete.html', {
            'article': article
        })
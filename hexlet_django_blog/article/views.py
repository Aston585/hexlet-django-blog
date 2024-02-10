from django.views import View
from django.shortcuts import render, get_object_or_404
from hexlet_django_blog.article.models import Article


class IndexView(View):
    template_name = 'articles/index.html'

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            self.template_name,
            context={
                'articles': articles,
            }
        )


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article,
        })

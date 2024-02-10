# from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from hexlet_django_blog.article.models import Article

# def index(request, article_id, tags):
#     return HttpResponse(f'Статья номер {article_id}. Тег {tags}')


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

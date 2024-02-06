from django.http import HttpResponse
# from django.views import View
# from django.shortcuts import render


def index(request, article_id, tags):
    return HttpResponse(f'Статья номер {article_id}. Тег {tags}')


# class IndexView(View):
#     template_name = 'articles/index.html'

#     def get(self, request):
#         return render(
#             request,
#             self.template_name,
#             context={'name': 'article'}
#         )

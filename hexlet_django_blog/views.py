from django.shortcuts import render
# from django.shortcuts import redirect
# from django.urls import reverse
from django.views.generic import TemplateView

# def index(request):
#     return redirect(reverse('article',
#                             kwargs={'tags': 'python', 'article_id': 42}))


def about(request):
    return render(request, 'about.html')


class IndexView(TemplateView):
    template_name = "index.html"
    extra_context = {'who': 'World'}

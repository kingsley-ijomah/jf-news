from django.views import generic

from .models import Article


class ArticleListView(generic.ListView):
    model = Article


class ArticleDetailView(generic.DetailView):
    pass


class ArticleCreateView(generic.CreateView):
    model = Article
    fields = ["pub_date", "title", "content"]
    success_url = "/"


class ArticleUpdateView(generic.UpdateView):
    model = Article
    fields = ["pub_date", "title", "content"]
    success_url = "/"


class ArticleDeleteView(generic.DeleteView):
    pass

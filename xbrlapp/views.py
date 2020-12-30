from django.views.generic import ListView,DetailView
from .models import Post

class Index(ListView):
    model = Post

class Detail(DetailView):
    model = Post

from django.views.generic.edit import CreateView

class Create(CreateView):
    model = Post

    # 編集対象にするフィールド
    fields = ['title', 'body', 'category', 'tags']
from django.views.generic import ListView,DetailView
from .models import Post

class Index(ListView):
    model = Post

class Detail(DetailView):
    model = Post
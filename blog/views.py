from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

# Create your views here.
class PostLV(ListView):
    model = Post

class PostDV(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'description', 'image']
    success_url = reverse_lazy('blog_index')

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'description', 'image']
    success_url = reverse_lazy('blog_index')

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog_index')

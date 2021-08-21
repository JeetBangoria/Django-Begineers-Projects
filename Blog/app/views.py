from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from .models import *

# Create your views here.
class BlogListView(ListView):
    model=Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'

class BlogCreateView(CreateView):
    model=Post
    template_name='post_new.html'
    fields=['title','author','body']

class BlogUpdateView(UpdateView):
    model = Post
    template_name='post_edit.html'
    fields = ['title','body']

class BlogDeleteView(DeleteView):
    model=Post
    template_name='post_delete.html'
    success_url=reverse_lazy('home')
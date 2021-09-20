from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post

# Create your views here.


class HomePageView(ListView): 
   model = Post
   template_name = 'home.html'
   context_object_name = 'all__post'
   paginate_by = 1


class BlogDetailView(DetailView):  
   model = Post
   template_name = 'Blog/detail.html'
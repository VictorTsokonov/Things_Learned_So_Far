from django.shortcuts import render
from django.views import generic

from .models import Post


# Create your views here.
class BlogView(generic.DetailView):
    model = Post
    template_name = "blog.html"


class AboutView(generic.TemplateView):
    template_name = "about.html"


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_at")
    template_name = "home.html"

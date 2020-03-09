from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, UpdateView

from .models import Post
from .forms import PostForm

class HomeView(TemplateView):
    template_name = 'birdie/home.html'


class AdminView(LoginRequiredMixin, TemplateView):
    template_name = 'birdie/admin.html'


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'birdie/update.html'
    success_url = '/'

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'birdie/home.html'


class AdminView(LoginRequiredMixin, TemplateView):
    template_name = 'birdie/admin.html'

from django.shortcuts import render, get_list_or_404
from django.views import generic
from .models import Blog, Comment


class HomeView(generic.View):

    def get(self, request):
       posts = get_list_or_404(Blog)
       data = {
              "posts":posts
       }
       return render(request, 'home.html', context=data)

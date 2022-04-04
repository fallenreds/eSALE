from django.shortcuts import render
from django.http import HttpResponse
from django.template.context_processors import request
from django.views import View

from .models import Post, Category


class HomeView(View):
    def get(self, request):
        all_category = Category.objects.values('title','slug')
        post_list = Post.objects.values('title')
        print(post_list.query)
        return render(request, 'main/home.html', {'post_list': post_list, 'all_category':all_category})
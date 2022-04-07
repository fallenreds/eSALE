from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.context_processors import request
from django.views import View
from django.contrib.auth import login, authenticate
from .forms import UserCreationForm
from .models import Post, Category, MyUser


class HomeView(View):
    def get(self, request):
        all_category = Category.objects.values('title', 'slug')
        post_list = Post.objects.all().order_by("-views")[:8]
        return render(request, 'main/home.html', {'post_list': post_list, 'all_category': all_category,})


class PostDetail(View):
    def get(self, request, slug):
        all_category = Category.objects.values('title', 'slug')
        post = Post.objects.get(id=slug)
        user = MyUser.objects.get(id=post.author_id)
        return render(request, 'main/post.html', {'post': post, 'user': user, 'all_category': all_category})


class RegisterView(View):


    def get(self, request):
        form = {
            'form': UserCreationForm()
        }
        # print(UserCreationForm())
        return render(request, 'registration/register.html', form)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'registration/register.html', {'form': form})
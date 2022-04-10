from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.context_processors import request
from django.views import View
from django.contrib.auth import login, authenticate
from .forms import MyUserCreationForm, MyAuthenticationForm, NewPostForm
from .models import Post, Category, MyUser
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.core.files.base import ContentFile


class HomeView(View):
    def get(self, request):
        all_category = Category.objects.values('title', 'slug')
        post_list = Post.objects.all().order_by("-views")[:8]
        return render(request, 'main/home.html', {'post_list': post_list, 'all_category': all_category, })


class PostDetail(View):
    def get(self, request, slug):
        all_category = Category.objects.values('title', 'slug')
        post = Post.objects.get(id=slug)
        user = MyUser.objects.get(id=post.author_id)
        return render(request, 'main/post.html', {'post': post, 'user': user, 'all_category': all_category})


class LoginView(View):
    def get(self, request):
        form = {
            'form': MyAuthenticationForm()
        }
        return render(request, 'registration/login.html', {'form': MyAuthenticationForm()})

    def post(self, request):
        form = MyAuthenticationForm(request, request.POST)
        print(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
        else:
            form = MyAuthenticationForm()
            error = 'Форма не прошла валидацию'
            return render(request, 'registration/login.html', {'form': form, 'error': error})


class RegisterView(View):

    def get(self, request):
        form = {
            'form': MyUserCreationForm()
        }
        return render(request, 'registration/register.html', form)

    def post(self, request):
        form = MyUserCreationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            return render(request, 'registration/register.html', {'form': form})


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        favorite_post = Post.objects.filter(favorite=request.user.id)
        user_post = Post.objects.filter(author_id=request.user.id)

        return render(request, 'main/profile.html', {'favorite_post': favorite_post,'user_post': user_post})


class CreatePostView(LoginRequiredMixin,View):
    def get(self,request):
        form = {
            'form': NewPostForm()
        }
        return render(request, 'main/newpost.html', form)

    def post(self,request):
        form = NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('/')
        return HttpResponse('Братан, все фигня')
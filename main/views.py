from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import request
from django.views import View
from django.contrib.auth import login, authenticate
from .forms import *
from .models import Post, Category, MyUser
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Count


@login_required
def add_favorite(request, id):
    post = Post.objects.get(id=id)
    if post.favorite.filter(id=request.user.id).exists():
        post.favorite.remove(request.user)
    else:
        post.favorite.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    if comment.author.id == request.user.id:
        comment.delete()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        return redirect('home')

@login_required
def delete_post(request, id):
    post = Post.objects.get(id=id)
    if post.author.id == request.user.id:
        post.delete()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        return redirect('home')

def home_view(request):
    if request.method == 'POST':
        print(request.POST)
        post_list = Post.objects.annotate(view_count=Count('viewed')).order_by('-view_count').filter(title__icontains=request.POST['q'])
        if request.POST['minpr'] != '':
            post_list = post_list.filter(cost__gte=request.POST['minpr'])
        if request.POST['maxpr'] != '':
            post_list = post_list.filter(cost__lte=request.POST['maxpr'])
        if 'category' in request.POST:
            post_list = post_list.filter(category__title=request.POST['category'])

        return render(request, 'main/home.html', {'post_list': post_list})
    else:
        post_list = Post.objects.annotate(view_count=Count('viewed')).order_by('-view_count')[:8]
        return render(request, 'main/home.html', {'post_list': post_list})


class PostDetail(View):
    def get(self, request, id):
        post = Post.objects.get(id=id)
        if request.user.is_authenticated:
            if not post.viewed.filter(id=request.user.id).exists():
                post.viewed.add(request.user.id)

        user = MyUser.objects.get(id=post.author_id)
        if post.favorite.filter(id=request.user.id).exists():
            flag = True
        else:
            flag = False

        context = {
            'user': user,
            'post': post,
            'flag': flag,
        }

        return render(request, 'main/post.html', context)
    # def post(self,request):


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
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
        if request.user.is_authenticated:
            return redirect('home')
        else:
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
    def get(self, request, id):
        comments = Comment.objects.filter(profile__id=id)
        if request.user.id == id:
            favorite_post = Post.objects.filter(favorite=request.user.id)
            user_post = Post.objects.filter(author_id=request.user.id)
            context = {
                'favorite_post': favorite_post,
                'user_post': user_post,
                'comments': comments
            }
        else:
            user = MyUser.objects.get(id=id)
            user_post = Post.objects.filter(author_id=id)
            form = CreateCommentForm()
            context = {
                'user_post': user_post,
                'user': user,
                'form': form,
                'comments': comments
            }
        return render(request, 'main/profile.html', context)

    def post(self, request, id):
        form = CreateCommentForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.profile = MyUser.objects.get(id=id)
            form.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        else:
            form = CreateCommentForm()
            return render(request, request.META['HTTP_REFERER'], {'form': form})




class CreatePostView(LoginRequiredMixin, View):
    def get(self, request):
        form = {
            'form': NewPostForm()
        }
        return render(request, 'main/newpost.html', form)

    def post(self, request):
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('/')
        return HttpResponse('Братан, все фигня')

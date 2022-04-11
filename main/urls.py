from django.urls import path
from . import views
from .forms import AuthenticationForm

urlpatterns = [
    path('', views.home_view, name="home"),
    path('post/<int:slug>', views.PostDetail.as_view(), name="post"),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    # path('profile/<int:id>', views.ProfileView.as_view(), name='profile'),
    path('newpost/', views.CreatePostView.as_view(), name='newpost'),
    path('fav/<int:id>', views.add_favorite, name='favorite'),
]

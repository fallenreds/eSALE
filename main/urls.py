from django.urls import path
from . import views
from .forms import AuthenticationForm

urlpatterns = [
    path('', views.home_view, name="home"),
    path('post/<int:id>', views.PostDetail.as_view(), name="post"),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('profile/<int:id>', views.ProfileView.as_view(), name='profile'),
    path('newpost/', views.CreatePostView.as_view(), name='newpost'),
    path('fv/<int:id>', views.add_favorite, name='favorite'),
    path('cm/<int:id>', views.delete_comment, name='dell_comment'),
    path('ps/<int:id>', views.delete_post, name='dell_post'),
]

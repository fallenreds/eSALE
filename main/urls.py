from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('post/<int:slug>', views.PostDetail.as_view(), name="post"),
]

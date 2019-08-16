from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('follower/', views.Follower.as_view(), name="home"),
    path('following/', views.Following.as_view(), name="home"),
]

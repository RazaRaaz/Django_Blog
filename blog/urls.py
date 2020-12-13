from django.urls import path
from . import views


urlpatterns = [
       path("", views.HomeView.as_view(), name="home"),
       path("register/", views.RegisterView.as_view(), name="register"),
       path("posts/<int:pk>", views.PostDetailView.as_view(), name="post_detail")
]
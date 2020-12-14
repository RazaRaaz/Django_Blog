from django.urls import path
from . import views


urlpatterns = [
       path("", views.HomeView.as_view(), name="home"),
       path("myposts/", views.MyPostsView.as_view(), name="myposts"),
       path("createpost/", views.CreatePostView.as_view(), name="create_post"),
       path("register/", views.RegisterView.as_view(), name="register"),
       path("posts/<int:pk>", views.PostDetailView.as_view(), name="post_detail")
]
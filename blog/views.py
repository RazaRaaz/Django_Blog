from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Blog, Comment
from .forms import RegisterForm, CreatePostForm


class HomeView(generic.View):

       def get(self, request):
              posts = get_list_or_404(Blog)
              total = Blog.objects.all().count()
              data = {
                     "posts":posts,
                     'total':total,
                     "user":request.user,
              }

              return render(request, 'home.html', context=data)



class MyPostsView(generic.View):
       def get(self, request):
              posts = Blog.objects.filter(owner=request.user)
              
              data = {
                     "posts":posts,
                     'total':posts.count(),
                     "user":request.user
              }

              return render(request, 'myposts.html', context=data)

       def post(self, request):
              return HttpResponse('POST request!')



class PostDetailView(generic.View):

       def get(self, request, pk):
              post = get_object_or_404(Blog, pk=pk)


              data = {
                     "post":post,
                     "user":request.user,
                     'like':post.like.filter(id=request.user.id).exists()
              }
              return render(request, 'post_detail.html', context=data)


       def post(self, request, pk):
              post = get_object_or_404(Blog, pk=pk)
              if post.like.filter(id=request.user.id).exists():
                     post.like.remove(request.user)
                     return redirect(f'/posts/{pk}')
              else:
                     post.like.add(request.user)
                     return redirect(f'/posts/{pk}')


class RegisterView(generic.View):
       def get(self, request):
              form = RegisterForm()
              data = {
                     "form":form
              }
              return render(request, 'registration/register.html', context=data)

       def post(self, request):
              
              form = RegisterForm(request.POST)

              if form.is_valid():

                     username = form.data['user_name']
                     email = form.data['email']
                     password = form.data['password']

                     if User.objects.filter(username=username) or User.objects.filter(username=username)  :
                            return render(
                                   request, 
                                   'registration/register.html', 
                                   context = {
                                          'error':"User Already Exists!",
                                          "form":RegisterForm()
                                   }
                            )
                            
                     else:                            
                            user = User.objects.create_user(
                                   username,
                                   email,
                                   password
                            )
                            user.save()
                            return redirect('/')
              



class CreatePostView(generic.View):
       
       def get(self, request):
              form = CreatePostForm()
              data = {
                     'form':form
              }
              return render(request, 'create_post.html', context=data)


       def post(self, request):
              
              form = CreatePostForm(request.POST, request.FILES)
              
              if form.is_valid():

                     title = form.cleaned_data.get("title")
                     short_body = form.cleaned_data.get("short_body")
                     blog_img = form.cleaned_data.get("blog_img")
                     body = form.cleaned_data.get("body")

                     post = Blog.objects.create(
                            owner=request.user,
                            title=title,
                            short_body=short_body,
                            blog_img=blog_img,
                            body=body
                     )
                     post.save()
                     return redirect('/')
              else:
                     data = {
                            'form':form,
                            "error":"Invalid Post Data"
                     }
                     return render(request, 'create_post.html', context=data)
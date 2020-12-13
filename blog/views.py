from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.models import User
from .models import Blog, Comment
from .forms import RegisterForm




class HomeView(generic.View):

    def get(self, request):
       posts = get_list_or_404(Blog)
       total = Blog.objects.all().count()
       data = {
              "posts":posts,
              'total':total
       }
       return render(request, 'home.html', context=data)


class PostDetailView(generic.View):

    def get(self, request, pk):
       post = get_object_or_404(Blog, pk=pk)

       data = {
              "post":post,
       }
       return render(request, 'post_detail.html', context=data)


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
       
from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
       owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog")
       title = models.CharField(max_length=1000)
       blog_img = models.ImageField(upload_to = 'pic_folder/')
       body = models.TextField()
       like = models.ManyToManyField(User, related_name='blog_posts', blank=True)
       created_time = models.DateTimeField(auto_now_add=True, null=True)

       def get_likes(self):
              return "\n".join([str(p) for p in self.like.all()])


class Comment(models.Model):
       owner = models.ForeignKey(User, on_delete=models.CASCADE)
       blog = models.ForeignKey(
              Blog, 
              on_delete=models.CASCADE, 
              related_name="comnents"
       )
       body = models.TextField()
       like = models.ManyToManyField(User, related_name="blog_comments", blank=True)
       created_time = models.DateTimeField(auto_now_add=True, null=True)

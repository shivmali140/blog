from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30,blank=True,null=True)
    date_joined = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.username
    
class Blog(models.Model):
    title = models.CharField(max_length=200, blank=False)
    content = models.TextField(blank=False)
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
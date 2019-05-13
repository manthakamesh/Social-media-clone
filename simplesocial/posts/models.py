from django.db import models
from django.urls import reverse
from django.conf import settings
#import misaka
from groups.models import Group
# Create your models here.
from django.contrib.auth import get_user_model
User=get_user_model()

class Post(models.Model):
    user=models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)
    message=models.TextField()
    message_html=models.TextField(editable=False)
    group=models.ForeignKey(Group,related_name='posts',null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.message_html=self.message#misaka.html(self.message)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username':self.user.username,'pk':self.pk})


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline

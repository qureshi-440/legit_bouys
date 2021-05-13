# from blog.views import profile
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
import datetime
from ckeditor.fields import RichTextField 
from django.utils.text import slugify
from .utils import modelsnippet
from hitcount.models import HitCount,HitCountMixin
from django.contrib.contenttypes.fields import GenericRelation
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.SET_NULL)
    profilepic = models.ImageField(upload_to='images/profile_pics/',default='images/profile_pics/default.png')
    bio = models.TextField()
    website_url = models.URLField(null=True,blank=True)
    facebook_url = models.URLField(null=True,blank=True)
    instagram_url = models.URLField(null=True,blank=True)
    twitter_url = models.URLField(null=True,blank=True)
    pintrest_url = models.URLField(null=True,blank=True)
    follow = models.ManyToManyField(User,blank=True,related_name="follows")

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("blog:home")

    @property
    def total_followers(self):
        return self.follow.count()

    @property
    def follower_names(self):
        follower_list = []
        for a in self.follow.all():
            follower_list.append(a)
        return follower_list
        # return " , ".join(a.username for a in self.follow.all())

    @receiver(post_save,sender=User)
    def create_profile(sender,instance,created,**kwargs):
        if created:
            UserProfile.objects.create(user=instance)


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    category = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now=True)
    body = RichTextField()
    auther = models.ForeignKey(User,on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to = 'images/post_thumbnails/',null=True,blank=True)
    snippet = models.TextField(max_length=255)
    like = models.ManyToManyField(User,related_name='blog_posts')
    # views = models.IntegerField(default=0)
    Hit_count_generic = GenericRelation(HitCount,object_id_field='object_pk',related_query_name='hit_count_generic_relation')


    @property
    def get_likes(self):
        return self.like.count()

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        self.snippet = modelsnippet(self.body)
        return super().save(*args,**kwargs)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:home")

    class Meta:
        ordering = ["-created_date"]

class Comments(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey('Post',on_delete=models.CASCADE,related_name='comments')
    time = models.DateTimeField(auto_now=True)
    message = models.TextField()

    def __str__(self):
        return str((self.post.title) + "  -- @" + self.User.username)

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={'slug':self.post.slug})

    class Meta:
        ordering = ["-time"]
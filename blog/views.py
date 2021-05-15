from django.shortcuts import render,get_object_or_404,reverse
from django.views.generic import CreateView,UpdateView,ListView,DeleteView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionDenied
from .models import UserProfile,Post,Comments
from django.contrib.auth.models import User
from .forms import UserProfileForm,PostCreateForm,PostUpdateForm,CommentForm
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from hitcount.views import HitCountDetailView
from django.contrib.auth.decorators import login_required

class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'

    def get_context_data(self,*args,**kwargs):
        data = super().get_context_data(*args,**kwargs)
        # data['snippet'] = homeSnippet()
        return data

class profile(CreateView,LoginRequiredMixin):
    model = UserProfile
    template_name = 'blog/profile_create.html'
    form_class = UserProfileForm

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def profile_page(request,username):
    user_profile = get_object_or_404(User,username=username)
    user_posts = Post.objects.filter(auther__username__iexact=username)
    user_follow = False
    if user_profile.userprofile.follow.filter(id=request.user.id).exists():
        user_follow = True
    return render(request,'blog/profile_page.html',{"user_profile":user_profile,'user_posts':user_posts,'user_follow':user_follow})

class update_profile(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'blog/profile_create.html'

    def get_object(self,*args,**kwargs):
        obj = super().get_object(*args,**kwargs)
        if obj.user != self.request.user:
            raise PermissionDenied()
        return obj

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class postcreate(CreateView,LoginRequiredMixin):
    model = Post
    form_class = PostCreateForm
    template_name = 'blog/post_create.html'

    def form_valid(self,form):
        form.instance.auther = self.request.user
        form.instance.created_date = datetime.datetime.now()
        return super().form_valid(form)

class postdetail(HitCountDetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail2.html'
    count_hit = True

    def get_context_data(self,*args,**kwargs):
        data = super().get_context_data(*args,**kwargs)
        post = get_object_or_404(Post,slug=self.kwargs['slug'])
        liked = False
        if post.like.filter(id=self.request.user.id).exists():
            liked = True
        
        data['all_posts'] = Post.objects.all
        data['liked'] = liked
        data["comments"] = Comments.objects.filter(post=post)
        return data


@login_required
def likeview(request,pk):
    post = get_object_or_404(Post,id=pk)
    liked = False
    if post.like.filter(id=request.user.id).exists():
        post.like.remove(request.user)
        liked = False
    else:
        post.like.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('blog:post_detail', kwargs={'slug':post.slug} ))

class postUpdate(UpdateView,LoginRequiredMixin):
    model = Post
    form_class = PostUpdateForm
    template_name = 'blog/post_update.html'

    def get_object(self,*args,**kwargs):
        obj = super().get_object(*args,**kwargs)
        if obj.auther != self.request.user:
            raise PermissionDenied()
        return obj

class postDelete(DeleteView,LoginRequiredMixin):
    model = Post
    template_name = 'blog/post_delete_confirm.html'
    success_url = reverse_lazy("blog:home")

    def get_object(self,*args,**kwargs):
        obj = super().get_object(*args,**kwargs)
        if obj.auther != self.request.user:
            raise PermissionDenied()
        return obj

class CommentCreate(CreateView,LoginRequiredMixin):
    model = Comments
    form_class = CommentForm
    
    def form_valid(self,form,**kwargs):
        post = get_object_or_404(Post,slug=self.kwargs['slug'])
        form.instance.User = self.request.user
        form.instance.time = datetime.datetime.now()
        form.instance.post = post
        form.save()
        return super().form_valid(form,**kwargs)
    
class CommentDelete(DeleteView,LoginRequiredMixin):
    model = Comments
    
    def get_object(self,*args,**kwargs):
        obj = super().get_object(*args,**kwargs)
        if obj.User != self.request.user:
            raise PermissionDenied()
        return obj

@login_required
def follow_user(request,pk):
    profile = get_object_or_404(UserProfile,id=pk)
    if profile.follow.filter(id=request.user.id).exists():
        profile.follow.remove(request.user)
    else:
        profile.follow.add(request.user)
    return HttpResponseRedirect(reverse("blog:profile_page",kwargs={'username':profile.user.username}))
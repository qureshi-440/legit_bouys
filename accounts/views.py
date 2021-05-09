from django.shortcuts import render,reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView
from django.contrib.auth import authenticate,login,get_user_model
from .models import User
from . import forms
from django.http import HttpResponseRedirect
# Create your views here.


class register(CreateView):
    # model = User
    form_class = forms.registerForm
    template_name = "registrations/register.html"
    success_url = reverse_lazy("blog:profile_create")

    def form_valid(self,form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username= form.cleaned_data['username'],password= form.cleaned_data["password1"])
        login(self.request,user)
        return HttpResponseRedirect(reverse("blog:profile_create"))

# class Allusers(ListView):
#     model = User
#     template_name='registrations/all_users.html'
#     context_object_name = 'user_list'

def Allusers(request):
    User = get_user_model() 
    users = User.objects.all()
    return render(request,'registrations/all_users.html',{'users':users})
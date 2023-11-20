from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout
from .forms import MyUserCreationForm, MyUserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class UserLogoutView(View):
    
    def get(self, request):
        return render(request, "registration/logout.html")
    
    
    def post(self, request):
        logout(request)
        return redirect("login")


class SignUpView(View):
    def get(self, request):
        form = MyUserCreationForm()
        return render(request, "registration/signup.html", {"form":form})
    
    def post(self, request):
        form = MyUserCreationForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
           return render(request, "registration/signup.html", {"form":form}) 
    
    
class UserUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        form = MyUserChangeForm(instance=request.user)
        return render(request, "registration/user_update.html", {"form":form})
    
    def post(self, request):
        form = MyUserChangeForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
           return render(request, "registration/user_update.html", {"form":form}) 
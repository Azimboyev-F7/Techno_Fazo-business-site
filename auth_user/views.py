from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MyAuthenticationForm, MyUserCreationForm
# Create your views here.

from django.contrib.auth import authenticate, login, logout


def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in')
        return redirect('main:index')
    forms = MyAuthenticationForm()
    if request.method == 'POST':
        forms = MyAuthenticationForm(request, data=request.POST)
        if forms.is_valid():
            user = forms.get_user() 
            if user is not None:
                login(request, user)  # `user` mavjudligini tekshirib login qilamiz
                messages.success(request, f'{user} are logged in')
                return redirect('main:index')
    context = {
        'form': forms
    }
    return render(request, 'auth/login.html', context)


def logout_view(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'You are not logged in')
        return redirect('auth_user:login')
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You are logged out')
        return redirect('main:index')
    
    ctx = {
        
    }
    return render(request, 'auth/logout.html', ctx)

def register_view(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in')
        return redirect('main:index')
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully')
            return redirect('auth_user:login')
    ctx = {
        'form': form
    }

    return render(request, 'auth/register.html', ctx)

from django.shortcuts import render, redirect
from .forms import MyAuthenticationForm, MyUserCreationForm
# Create your views here.

from django.contrib.auth import authenticate, login, logout


def login_view(request):
    forms = MyAuthenticationForm()
    if request.method == 'POST':
        forms = MyAuthenticationForm(request, data=request.POST)
        if forms.is_valid():
            user = forms.get_user() 
            print(f"Authenticated user: {user}")  # 🔍 Tekshirish uchun qo‘shilgan qator
            if user is not None:
                login(request, user)  # `user` mavjudligini tekshirib login qilamiz
                return redirect('main:index')
    context = {
        'form': forms
    }
    return render(request, 'auth/login.html', context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('main:index')
    
    ctx = {
        
    }
    return render(request, 'auth/logout.html', ctx)

def register_view(request):
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auth_user:login')
    ctx = {
        'form': form
    }

    return render(request, 'auth/register.html', ctx)

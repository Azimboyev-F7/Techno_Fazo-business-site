from django.shortcuts import render, redirect
from .forms import MyAuthenticationForm
# Create your views here.

from django.contrib.auth import authenticate, login, logout


def login_view(request):
    forms = MyAuthenticationForm()
    if request.method == 'POST':
        forms = MyAuthenticationForm(request, data=request.POST)
        if forms.is_valid():
            user = forms.get_user() 
            login(request, user)
            return redirect('main:index')
    context = {
        'forms': forms
    }
    return render(request, 'auth_user/login.html', context)

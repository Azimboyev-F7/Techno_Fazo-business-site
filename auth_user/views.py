from django.shortcuts import render

# Create your views here.

from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import AuthenticationFailed


def login_view(request):
    context = {

    }
    return render(request, 'auth_user/login.html', context)

from django.urls import path
from .views import login

app_name = 'auth_user'

urlpatterns = [
    # path('register/', register, name='register'),
    path('login/', login, name='login'),
]
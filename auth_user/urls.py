from django.urls import path
from .views import login_view, register_view, logout_view

app_name = 'auth_user'

urlpatterns = [
    # path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]
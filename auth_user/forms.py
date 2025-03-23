from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

class MyAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(MyAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'name': 'username',
            'placeholder': 'Enter your Username',
            'id': 'exampleFormControlUsername',
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'name': 'password',
            'placeholder': 'Enter your Password',
            'id': 'exampleFormControlPassword',
        })
        
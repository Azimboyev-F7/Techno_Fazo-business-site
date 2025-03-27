from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
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

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'name': 'username',
            'placeholder': 'Enter your Username',
            'id': 'exampleFormControlUsername',
            "required": True
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'name': 'email',
            'placeholder': 'Enter your Email',
            'id': 'exampleFormControlEmail',
            "required": True
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'name': 'password1',
            'placeholder': 'Enter your Password',
            'id': 'exampleFormControlPassword',
            "required": True
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'name': 'password2',
            'placeholder': 'Confirm your Password',
            'id': 'exampleFormControlConfirmPassword',
            "required": True
        })
        
from django.shortcuts import render

# Create your views here.

def index(request):
    context = {

    }
    return render(request, 'index.html', context)


def industry(request):
    context = {
    }
    return render(request, 'industries.html', context)

from django.shortcuts import render
from .forms import (
    CustomUserCreationForm,
    CustomLoginForm,
)

# Create your views here.
def signup(request):
    form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'users/signup.html', context)


def login(request):
    form = CustomLoginForm()
    context = {
        'form': form,
    }
    return render(request, 'users/login.html', context)
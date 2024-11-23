from django.shortcuts import render
from users.forms import LoginForms, SignupForms

def login(request):
    return render(request, 'users/login.html', {'form': LoginForms()})

def signup(request):
    return render(request, 'users/signup.html', {'form': SignupForms()})

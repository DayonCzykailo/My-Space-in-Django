from django.shortcuts import render, redirect
from users.forms import LoginForms, SignupForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            user = auth.authenticate(request=request, username=form['username'].value(), password=form['password'].value())

            if user is not None:
                auth.login(request, user)
                return redirect('home')
            
        messages.error(request, 'Usuário ou senha inválidos')


    return render(request, 'users/login.html', {'form': LoginForms()})

def signup(request):
    form = SignupForms()

    if request.method == 'POST':
        form = SignupForms(request.POST)

        if form.is_valid():
            
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                messages.error(request, 'Usuário já cadastrado')
            
            
            if not messages.get_messages(request):
                user = User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'], password=form.cleaned_data['password'])
                user.save()

                messages.success(request, 'Usuário cadastrado com sucesso!')

                return redirect('login')
            
    return render(request, 'users/signup.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Deslogado com sucesso!')
    return redirect('login')
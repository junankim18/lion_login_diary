from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(
                request=request, username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('/')
        else:
            form = AuthenticationForm()
            ctx = {
                'form': form,
                'error': 'username or password is incorrect'
            }
            return render(request, 'account/login.html', ctx)

    else:
        form = AuthenticationForm()
        ctx = {
            'form': form
        }
        return render(request, 'account/login.html', ctx)


def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            form = RegisterForm()
            ctx = {
                'form': form,
                'error': 'username or password is incorrect'
            }
            return render(request, 'account/signup.html', ctx)

    else:
        form = RegisterForm()
        ctx = {
            'form': form
        }
        return render(request, 'account/signup.html', ctx)

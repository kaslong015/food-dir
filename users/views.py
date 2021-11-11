from .forms import LoginForm, SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user and user.is_user:
                login(request, user)
                return redirect('home')
            if user and user.is_restaurant:
                login(request, user)
                return redirect('dashboard')

    context = {'form': forms}
    return render(request, 'users/login1.html', context)


def signup_page(request):
    context = {}
    forms = SignUpForm()
    if request.method == 'POST':
        forms = SignUpForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password1 = forms.cleaned_data['password1']
            password2 = forms.cleaned_data['password2']
            email = forms.cleaned_data['email']
            user = User.objects.create_user(username, email, password1)
            user.save()
            user = authenticate(username=username, password=password1)
            if user:
                login(request, user)
                return redirect('login')

    context = {'form': forms}
    return render(request, 'users/signup.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from .forms import SignupForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('account:login')
    else:
        form = SignupForm()

    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

def login_check(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect
    else:
        form = AuthenticationForm()

    context = {
        'form':form
    }
    return render(request,'accounts/login.html',context)

def logout(request):
    django_logout(request)
    return redirect('/')
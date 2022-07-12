from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render

# from .forms import LoginForm


def login_page(request):
    form = AuthenticationForm(request, request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)

    return render(request, "login.html", {"form": form})


def logout_page(request):
    logout(request)
    return render(request, "login.html")


def register_page(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, "login.html", {"form": form})

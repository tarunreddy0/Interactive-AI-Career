from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomRegisterForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate


def register(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('careerbot:login')
    else:
        form = CustomRegisterForm()

    context = {'form': form}

    return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('careerbot:home')
        else:
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')
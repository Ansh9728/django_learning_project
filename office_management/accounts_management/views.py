from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

# Create your views here.

def register_view(request):

    if request.user.is_authenticated:
        return redirect('/')


    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            user = form.save()  # Save user to UserDatabase
            auth_login(request, user)
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account Created Successfully for {username}")
            return redirect('/')  # Redirect to home page or any other page after successful sign up
        else:
            messages.error(request, f"Account Creation Failed")
            return redirect("sign_up")
    else:
        form = UserRegistrationForm()  # Initialize the form for GET requests
    
    return render(request, 'registration/sign_up.html', context={'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, f"Login Successful {username}")
            return redirect('/')
        else:
            messages.warning(request, 'Invalid username or password. Please try again.')
    
    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)

    return redirect('/')
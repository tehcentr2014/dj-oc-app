from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth 
from django.http import HttpResponse
from django.contrib import messages

##Other AUTH Imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# Create your views here

def anonymous_required(function=None, redirect_url=None):

    if not redirect_url:
        redirect_url = 'dashboard'

    actual_decorator = user_passes_test(
        lambda u: u.is_anonymous,
        login_url=redirect_url
    )

    if function:
        return actual_decorator(function)
    return actual_decorator    

@anonymous_required
def login(request):
    if request.method == 'POST':
        email = request.POST['email'].replace(' ', '').lower()
        password = request.POST['password']

        # Authenticate using email as username
        user = auth.authenticate(username=email, password=password)  # Correct authentication
 

        if user:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid Credentials or User does not exist")
            return redirect('login')  # Redirect to login instead of register if credentials are invalid

    return render(request, 'authorisation/login.html', {})

def home(request):
    return render(request, 'landing/index.html', {})

@anonymous_required
def register(request):
    if request.method == 'POST':
        email = request.POST['email'].replace(' ', '').lower()
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords don't match")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, f"A user with the email address: {email} already exists, please use a different email")
            return redirect('register')

        user = User.objects.create_user(email=email, username=email, password=password2)
        user.save()

        auth.login(request, user)
        return redirect('dashboard')

    return render(request, 'authorisation/register.html', {})

@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')



from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth 
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def login(request):
    return render(request, 'authorisation/login.html', {})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email'].replace(' ','').lower()
        password1 = request.post['password1']
        password2 = request.post['password2']

        if not password1 == password2:
            messages.error(request, "Password don't match")
            return redirect('register')


        if User.objects.filter(email=email).exists():
            messages.error(request,"A user with the email address: {} already exists, please use a different email".format(email))    
            return redirect('register')

        newUser.objects.create_user(email=email, username=email, password=password2)
        newUser.save()   

        auth.login(request,user)
        return redirect ('home')


        #print('Username submitted was: {}'.format(username))
    return render(request, 'authorisation/register.html', {})



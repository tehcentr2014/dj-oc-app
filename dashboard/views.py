from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth 
from django.http import HttpResponse
from django.contrib import messages

##Other AUTH Imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

##Local Imports
from .forms import *
from .models import *


# Create your views here.
@login_required
def home (request):

    context = {}
    return render(request, 'dashboard/home.html', context)

def profile(request):
    context = {}
    profile = user.profile

    # user = request.user
    # if hasattr(user, 'profile'):
    #     pass
    # else:
    #     profile=Profile.objects.create(user=user)

    if request.method == 'GET':
        form = ProfileForm(instance=request.user.profile)
        context['form'] = form
        return render(request, 'dashboard/profile.html', context)

    if request.method == 'POST':
        form  =  ProfileForm(request.POST, instance=request.user.profile)

        if form.is_valid():
            form.save()
            return redirect('profile')
            # obj = form.save(commit=False)
            # obj.user = request.user
            # obj.save()

    return render(request, 'dashboard/profile.html', context)

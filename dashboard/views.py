from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import messages

# Other AUTH Imports
from django.contrib.auth.decorators import login_required

# Local Imports
from .forms import *
from .models import *

# Create your views here.
@login_required
def home(request):
    context = {}
    return render(request, 'dashboard/home.html', context)

@login_required
def profile(request):
    context = {}
    user_profile = request.user.profile

    if request.method == 'GET':
        form = ProfileForm(instance=user_profile)
        image_form = ProfileImageForm(instance=user_profile)
        context['form'] = form
        context['image_form'] = image_form
        return render(request, 'dashboard/profile.html', context)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user_profile)
        image_form = ProfileImageForm(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
        if image_form.is_valid():
            image_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')    
        else:
            messages.error(request, 'Please correct the error below.')
            
    
    context['form'] = form  # In case of a POST request, we also need to pass the form to the context
    return render(request, 'dashboard/profile.html', context)
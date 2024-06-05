from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth 
from django.http import HttpResponse
from django.contrib import messages

##Other AUTH Imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
@login_required
def home (request):

    context = {}
    return render(request, 'dashboard/home.html', context)
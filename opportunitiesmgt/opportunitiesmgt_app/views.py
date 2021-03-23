from django.shortcuts import render, redirect, reverse 
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Account, Opportunitie

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm, OpportunitieForm, AccountForm

def index(request):
    return render(request, 'opportunitiesmgt/index.html')


def about_usPage(request):
    context = {}
    return render(request, "opportunitiesmgt/about_us.html", context)


def signupPage(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'opportunitiesmgt/signup.html', context)


def loginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            return redirect('userProfile')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'opportunitiesmgt/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('index')
    

def contact_usPage(request):
    context = {}
    return render(request, "opportunitiesmgt/contact_us.html", context)

#@login_required(login_url='login')
def userProfile(request):
    accounts = Account.objects.all()
    opportunities = Opportunitie.objects.all()

    context = {'accounts':accounts, 'opportunities':opportunities}
    return render(request, "opportunitiesmgt/userProfile.html", context)


def create_account(request):
    if request.method == 'POST':
        form=AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userProfile')
    else:
        form = AccountForm()

    context = {'form': form}
    return render(request, 'opportunitiesmgt/create_account_form.html', context)


def create_opportunity(request):
    if request.method == 'POST':
        form=OpportunitieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userProfile')
    else:
        form = OpportunitieForm()

    context = {'form': form}
    return render(request, 'opportunitiesmgt/create_opportunities_form.html', context)
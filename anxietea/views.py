from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def onboarding(request):
    return render(request, 'anxietea/onboarding.html')

def emotions_view(request):
    return render(request, 'anxietea/emotions.html' )

def login_view(request):
    # username, password = request.POST['username'], request.POST['password']
    # user = authenticate(username=username, password=password)
    # if user is not None:
    #     login(request, user)
    #     return redirect('/')
    # else:
    #     return redirect('/splash?error=LoginError')
    return render(request, 'anxietea/login.html' )

def signup_view(request):
    # user = User.objects.create_user(
    #     username=request.POST['username'],
    #     password=request.POST['password'],
    #     email=request.POST['email'],
    # )
    # login(request, user)
    # return redirect('/')
    return render(request, 'anxietea/signup.html')

def logout_view(request):
    logout(request)
    return redirect('/splash')

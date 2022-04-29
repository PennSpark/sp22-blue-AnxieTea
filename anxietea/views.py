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
    return render(request, 'anxietea/login.html' )

def sleep_view(request):
    return render(request, 'anxietea/sleep.html' )

def mood_view(request):
    return render(request, 'anxietea/mood-home.html' )

def analysis_view(request):
    return render(request, 'anxietea/analysis.html' )

def login_submit(request):
    username, password = request.POST['username'], request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/home')
    else:
        return redirect('/login?error=LoginError')

def signup_view(request):
    return render(request, 'anxietea/signup.html')

def home_view(request):
    user = request.user
    if user is not None:
        login(request, user)
        return render(request, 'anxietea/home.html' )
    else:
        return redirect(request, 'anxietea/onboarding.html')


def signup_submit(request):
    user = User.objects.create_user(
        username=request.POST['username'],
        password=request.POST['password'],
        email=request.POST['email'],
        age=request.POST['age'],
        gender=request.POST['gender']
    )
    login(request, user)
    return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('/')

def profile_view(request):
    user = request.user

    return render(request, 'anxietea/profile.html', { user: user})
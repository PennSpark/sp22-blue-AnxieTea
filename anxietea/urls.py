from django.urls import path
from . import views

urlpatterns = [
    path('', views.onboarding, name='onboarding'),
    path('emotions/', views.emotions_view, name='emotions_view'),
    path('login/', views.login_view, name='login_view'),
    path('login_submit/', views.login_submit, name='login_submit'),
    path('signup/', views.signup_view, name='signup_view'),
    path('signup_submit/', views.signup_submit, name='signup_submit'),
    path('logout/', views.logout_view, name='logout_view'),
    path('profile/', views.profile_view, name='profile_view'),
]

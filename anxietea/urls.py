from django.urls import path
from . import views

urlpatterns = [
    path('', views.onboarding, name='onboarding'),
    path('emotions/', views.emotions_view, name='emotions_view'),
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('logout/', views.logout_view, name='logout_view'),
]

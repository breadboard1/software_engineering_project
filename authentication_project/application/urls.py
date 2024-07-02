from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign_up/', views.sign_up, name='signup'),
    path('log_in/', views.log_in, name='login'),
    path('log_out/', views.log_out, name='logout'),
    path('change_pass/', views.change_pass, name='changepass'),
    path('change_pass_without_old_pass/', views.change_pass_without_old_pass, name='changepasswithoutoldpass'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='updateprofile'),
]

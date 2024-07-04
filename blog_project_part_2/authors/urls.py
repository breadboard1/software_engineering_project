from django.urls import path
from . import views

urlpatterns = [
    path('sign_up/', views.sign_up, name='signup'),
    path('log_in/', views.log_in, name='login'),
    path('log_out/', views.log_out, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='editprofile'),
    path('change_password/', views.change_password, name='changepassword'),
]
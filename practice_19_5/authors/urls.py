from django.urls import path
from . import views

urlpatterns = [
    path('sign_up/', views.sign_up, name='signup'),
    path('log_in/', views.UserLoginView.as_view(), name='login'),
    path('log_out/', views.UserLogOutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
]
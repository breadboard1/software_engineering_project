from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('sign_up/', views.sign_up, name='signup'),
    path('sign_in/', views.UserLogInView.as_view(), name='signin'),
    path('sign_out/', views.UserLogOutView.as_view(), name='signout'),
    path('edit_profile/', views.edit_profile, name='editprofile'),
    path('change_password/', views.change_password, name='changepassword'),
    path('buy_now/<int:id>', views.buy_now, name='buynow'),
]

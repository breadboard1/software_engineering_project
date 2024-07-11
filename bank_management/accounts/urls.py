from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.UserRegistrationView.as_view(), name='registration'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='meal'),
    path('/pricing', views.pricing, name='pricing'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('car_details/<int:id>/', views.DetailCarView.as_view(), name='cardetails'),
]
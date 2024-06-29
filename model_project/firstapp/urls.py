from django.urls import path
from . import views

urlpatterns = [
    path('', views.newhome, name='newhome'),
    # path('delete/<int:roll>', views.delete_student, name='delete_student'),
]

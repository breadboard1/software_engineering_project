from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_category, name='add_category'),
    # path('edit_category/<int:id>', views.edit_category, name='edit_category'),
]

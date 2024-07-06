from django.shortcuts import render, redirect
from cars.models import Car
from brands.models import Brands

def home(request, brand_slug = None):
    cars = Car.objects.all()
    if brand_slug is not None:
        brand = Brands.objects.get(slug = brand_slug)
        cars = Car.objects.filter(brand = brand)
    brands = Brands.objects.all()
    return render(request, './home.html', {'cars':cars, 'brands':brands})
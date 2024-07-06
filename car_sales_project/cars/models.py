from django.db import models
from django.contrib.auth.models import User
from brands.models import Brands

# Create your models here.
class Car(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField(null=True)
    image = models.ImageField(upload_to="uploads/")
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Comment by {self.name}'


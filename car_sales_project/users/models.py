from django.db import models
from django.contrib.auth.models import User
from cars.models import Car

# Create your models here.
class Buy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}'
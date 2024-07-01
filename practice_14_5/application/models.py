from django.db import models

# Create your models here.
class ExampleModel(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField()
    time = models.DateTimeField
    yes_or_no = models.BooleanField()
    comment = models.TextField()
    email = models.EmailField()

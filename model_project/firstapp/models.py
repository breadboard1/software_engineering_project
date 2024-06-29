from django.db import models

# Create your models here.
class Student(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=20)
    address = models.TextField()
    def __str__(self) -> str:
        return f'Roll : {self.roll} - {self.name}'


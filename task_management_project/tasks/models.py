from django.db import models
from categories.models import Category

# Create your models here.
class Task(models.Model):
    task_title = models.CharField(max_length=300)
    task_description = models.TextField()
    is_completed = models.BooleanField(default=False)
    task_assign_date = models.DateField()
    category = models.ManyToManyField(Category)
    def __str__(self) -> str:
        return self.task_title


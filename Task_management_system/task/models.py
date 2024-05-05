from django.db import models
from category.models import CategoryModel

# Create your models here.
class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=250)
    taskDescription = models.TextField()
    categories = models.ManyToManyField(to=CategoryModel)
    is_completed = models.BooleanField(default=False)
    TaskAssignDate = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.taskTitle
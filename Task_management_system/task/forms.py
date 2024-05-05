from django import forms
from . import models


class TaskForm(forms.ModelForm):

    class Meta:
        model = models.TaskModel
        exclude = ('TaskAssignDate', )
        labels = {
            'taskTitle': 'Title',
            'taskDescription': 'Description',
            'is_completed': 'Complete'
        }

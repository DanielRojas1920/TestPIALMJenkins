from django import forms
from .models import Task

class TaskRegistrationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'due_date']

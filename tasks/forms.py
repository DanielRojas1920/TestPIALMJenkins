from django import forms
from .models import Task

class TaskRegistrationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'due_date', 'description',]

        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea,
        }

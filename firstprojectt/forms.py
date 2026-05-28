from django import forms
from firstprojectt.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["task", "is_completed"]

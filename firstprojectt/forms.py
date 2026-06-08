from django import forms
from firstprojectt.models import Task
from firstprojectt.models import Information


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["task", "is_completed"]


class InformationForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ["First_Name", "SurName", "Age", "Gender", "Date_of_birth"]

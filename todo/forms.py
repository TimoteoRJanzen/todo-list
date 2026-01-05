from django import forms

from todo.models import Task


class TodoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]

        widgets = {
            "tags": forms.CheckboxSelectMultiple(),
        }

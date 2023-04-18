from django.forms import ModelForm
from todos.models import TodoList
from django import forms


class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ["name"]

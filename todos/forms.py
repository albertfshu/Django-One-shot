from django.forms import ModelForm
from todos.models import TodoList, TodoItem
from django import forms


class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ["name"]


class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ["task", "due_date", "is_completed", "list"]

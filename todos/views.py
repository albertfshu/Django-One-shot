from django.shortcuts import render
from todos.models import TodoList


# Create your views here.
def todo_list(request):
    todo_lists = TodoList.objects.all()
    context = {
        "todo_list": todo_lists,
    }
    return render(request, "todos/todo_list.html", context)

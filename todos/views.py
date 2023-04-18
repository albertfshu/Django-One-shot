from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList, TodoItem


# Create your views here.
def todo_list(request):
    todo_lists = TodoList.objects.all()
    context = {
        "todo_list": todo_lists,
    }
    return render(request, "todos/todo_list.html", context)


def todo_list_detail(request, id):
    todolist = get_object_or_404(TodoList, id=id)
    context = {"todolist": todolist}
    return render(request, "todos/todo_list_detail.html", context)


def create_todo_list(request, id):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            todo_list = form.save()
            return redirect(
                request,
                "todo_list_detail",
            )
    else:
        form = TodoListForm()

    context = {"form": form}
    return render(request, "todo_list/create_todo_list.html", context)

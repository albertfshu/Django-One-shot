from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList, TodoItem
from todos.forms import TodoListForm, TodoItemForm


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


def create_todo_list(request):
    form = TodoListForm(request.POST)
    if form.is_valid():
        todolist = form.save()
        return redirect("todo_list_detail", id=todolist.id)
    else:
        form = TodoListForm()

    context = {"form": form}

    return render(request, "todos/create_todo_list.html", context)


def edit_todo_list(request, id):
    edit = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        form = TodoListForm(request.POST, instance=edit)
        if form.is_valid():
            edit = form.save()
            return redirect("todo_list_detail", id=update.id)
    else:
        form = TodoListForm(instance=edit)
    context = {"form": form}
    return render(request, "todos/todo_list_update.html", context)


def delete_todo_list(request, id):
    todolist = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        todolist.delete()
        return redirect("todo_list")
    context = {"todolist": todolist}
    return render(request, "todos/delete_todo_list.html", context)


def create_todo_item(request):
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            todo_list = form.cleaned_data["list"]
            return redirect("todo_list_detail", id=todo_list.id)
    else:
        form = TodoItemForm()
    context = {
        "item_form": form,
    }

    return render(request, "todos/create_todo_item.html", context)

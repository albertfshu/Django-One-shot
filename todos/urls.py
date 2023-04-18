from django.urls import path
from todos.views import (
    todo_list,
    todo_list_detail,
    create_todo_list,
    edit_todo_list,
)


urlpatterns = [
    path("", todo_list, name="todo_list_list"),
    path("<int:id>/", todo_list_detail, name="todo_list_detail"),
    path("create/", create_todo_list, name="todo_list_create"),
    path("<int:id>/edit/", edit_todo_list, name="todo_list_update"),
]

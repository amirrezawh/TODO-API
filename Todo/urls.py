from django.urls import path
from .views import (TodoListView,TodoView,
TodoShowView, TodoDelete, TodoUpdate,
TodoArchiveList)

app_name = "TodoApp"

urlpatterns = [
    path('list/', TodoListView.as_view(),
    name="todo-list"),
    
    path('add/', TodoView.as_view(),
    name="todo-view"),

    path('show/<id>/',TodoShowView.as_view(),
    name="todo-show"),

    path('delete/<id>/', TodoDelete.as_view(),
    name="todo-delete"),

    path('update/<id>/', TodoUpdate.as_view(),
    name="todo-update"),

    path('list/archive/', TodoArchiveList.as_view(),
    name="todo-archive-list"),
]
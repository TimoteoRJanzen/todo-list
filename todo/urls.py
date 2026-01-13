from django.urls import path

from todo.views import (
    TodoListView,
    TodoCreateView,
    TodoUpdateView,
    TodoDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    ToggleTaskStatusView,
)

app_name = "todo"

urlpatterns = [
    path("", TodoListView.as_view(), name="todo-list"),
    path("create/", TodoCreateView.as_view(), name="todo-create"),
    path("update/<int:pk>/", TodoUpdateView.as_view(), name="todo-update"),
    path("delete/<int:pk>/", TodoDeleteView.as_view(), name="todo-delete"),
    path("toggle/<int:pk>/", ToggleTaskStatusView.as_view(), name="task-toggle"),

    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/update/<int:pk>/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/delete/<int:pk>/", TagDeleteView.as_view(), name="tag-delete"),

]
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View

from todo.forms import TodoForm
from todo.models import Task, Tag


class TodoListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")


class TodoCreateView(generic.CreateView):
    model = Task
    form_class = TodoForm
    success_url = reverse_lazy("todo:todo-list")


class TodoUpdateView(generic.UpdateView):
    model = Task
    form_class = TodoForm
    success_url = reverse_lazy("todo:todo-list")


class TodoDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:todo-list")


class ToggleTaskStatusView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.done = not task.done
        task.save()
        return redirect("todo:todo-list")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")

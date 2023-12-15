from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Todo

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello World</h1>")

class TodoList(ListView):
    model = Todo
    context_object_name = "tasks"
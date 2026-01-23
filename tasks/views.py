from django.shortcuts import render
from tasks.models import Task

# Create your views here.
def tasks_view(request):
    tasks = Task.objects.filter(user=request.user).order_by("nome_task")
    return render(request,"tasks/tasks.html",{"tasks":tasks})

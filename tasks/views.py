from django.shortcuts import render,redirect
from tasks.models import Task

# Create your views here.
def tasks_view(request):
    tasks = Task.objects.filter(user=request.user).order_by("nome_task")
    return render(request,"tasks/tasks.html",{"tasks":tasks})

def add_tasks(request):
    if request.method == "POST":
        Task.objects.create(
            nome_task = request.POST.get("nome_task"),
            data_inicio = request.POST.get("data_inicio"),
            data_fim = request.POST.get("data_fim"),
            descricao = request.POST.get("descricao"),
            user = request.user
        )
    return redirect("tasks")

def delete_task(request):
    if request.method == "POST":
        task_id = request.POST.get("task_id")
        Task.objects.filter(
            id=task_id,
            user = request.user
        ).delete()
    return redirect("tasks")
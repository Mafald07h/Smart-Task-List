from django.contrib import admin
from tasks.models import Task

# Register your models here.
@admin.register(Task)
class TasksAdmin(admin.ModelAdmin):
    list_display = ("nome_task","data_inicio","data_fim","descricao")
    search_fields = ("nome_task",)
    list_filter = ("nome_task",)
"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from dashboard.views import dashboard
from tasks.views import tasks_view,add_tasks,delete_task,editar_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/',dashboard,name="dashboard"),
    path('',include('accounts.urls')),
    path('tasks/',tasks_view,name="tasks"),
    path('add_task/',add_tasks,name="add_task"),
    path('delete_task',delete_task,name="delete_task"),
    path('editar_task/',editar_task,name='editar_task'),
    path('accounts/',include('allauth.urls')),
]

from django.urls import path
from accounts.views import sign_in,sign_up

urlpatterns = [
    path('',sign_in,name="login"),
    path('cadastro/',sign_up,name="cadastro")
]
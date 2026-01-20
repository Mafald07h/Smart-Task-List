from django.urls import path
from accounts.views import sign_in,sign_up,logout_account

urlpatterns = [
    path('',sign_in,name="login"),
    path('cadastro/',sign_up,name="cadastro"),
    path('logout/',logout_account,name="logout_account")
]
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.models import User
from accounts.forms import LoginForm,CadastroForm

# Create your views here.
def sign_in(request):
    form = LoginForm(request.POST)
    if request.method == "POST":
        username = form["username"].value()
        senha = form["senha"].value()

        user = authenticate(
            request,
            username=username,
            password=senha
        )

        if user is not None:
            login(request,user)
            messages.success(request,f"Bem vindo(a) {username}")
            return redirect("dashboard")
        else:
            messages.error(request,"Usuário ou senha incorretos")
            return redirect("login")
    return render(request,"accounts/sign-in.html",{"form":form})

def sign_up(request):
    form = CadastroForm(request.POST)
    if request.method == "POST":
        username = form["username"].value()
        email = form["email"].value()
        senha1 = form["senha1"].value()
        senha2 = form["senha2"].value()

        if senha1 != senha2:
            messages.error(request,"As senhas precisam ser iguais.")
            return redirect("cadastro")
        if User.objects.filter(username=username).exists():
            messages.error(request,"Usuário já cadastrado.")
            return redirect("cadastro")
        if User.objects.filter(email=email).exists():
            messages.error(request,"Email já cadastrado.")
            return redirect("cadastro")
        
        user = User.objects.create_user(username=username,password=senha1,email=email)
        user.save()
        return redirect("login")
    return render(request,"accounts/sign-up.html")

def logout_account(request):
    logout(request)
    messages.success(request,"Logout realizado com sucesso!!")
    return redirect("login")
from django.shortcuts import render

from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages


def index(request):
    return render(request,'index.html',{
        #context
    })

def login_view(request):
    return render(request, 'login.html',{
        
     })


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else: 
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'login.html',{

    })
    
def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión finalizada')
    return redirect('login')

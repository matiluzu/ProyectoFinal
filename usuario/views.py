from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login

# Create your views here.

def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            contrasenia = formulario.cleaned_data['password']
            
            user=authenticate(username=usuario, password=contrasenia)
            
            django_login(request, user)
            return redirect('inicio:inicio')
        else:
            return render(request, 'usuario/login.html', {'formulario':formulario})
    
    formulario = AuthenticationForm()
    return render(request, 'usuario/login.html', {'formulario':formulario})

def signup(request):
    
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('usuario:login')
        else:
            return render(request, 'usuario/signup.html', {'formulario':formulario})

    formulario = UserCreationForm()
    return render(request, 'usuario/signup.html', {'formulario':formulario})
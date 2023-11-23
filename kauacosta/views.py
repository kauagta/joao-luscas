from django.shortcuts import render
from .models import Usuario


def home(request):
    return render(request, 'usuarios/usuarios.html')

def usuario(request):
    return render(request, 'usuario.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_Usuario = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    usuarios = {
        'usuarios':Usuario.objects.all()
    
    }
    

    return render(request,'usuarios/usuarios.html')
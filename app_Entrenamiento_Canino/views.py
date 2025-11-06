from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente

def inicio_entrenamiento_canino(request):
    return render(request, 'inicio.html')

def agregar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        email = request.POST['email']
        fecha_registro = request.POST['fecha_registro']
        fecha_nacimiento = request.POST['fecha_nacimiento']
        comentarios = request.POST.get('comentarios', '')
        
        cliente = Cliente(
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            email=email,
            fecha_registro=fecha_registro,
            fecha_nacimiento=fecha_nacimiento,
            comentarios=comentarios
        )
        cliente.save()
        return redirect('ver_cliente')
    
    return render(request, 'clientes/agregar_cliente.html')

def ver_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/ver_cliente.html', {'clientes': clientes})

def actualizar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    return render(request, 'clientes/actualizar_cliente.html', {'cliente': cliente})

def realizar_actualizacion_cliente(request, id_cliente):
    if request.method == 'POST':
        cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
        cliente.nombre = request.POST['nombre']
        cliente.direccion = request.POST['direccion']
        cliente.telefono = request.POST['telefono']
        cliente.email = request.POST['email']
        cliente.fecha_registro = request.POST['fecha_registro']
        cliente.fecha_nacimiento = request.POST['fecha_nacimiento']
        cliente.comentarios = request.POST.get('comentarios', '')
        cliente.save()
        return redirect('ver_cliente')
    
    return redirect('ver_cliente')

def borrar_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_cliente')
    
    return render(request, 'clientes/borrar_cliente.html', {'cliente': cliente})
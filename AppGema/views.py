from django.shortcuts import render
from AppGema.models import Habitacion
from AppGema.forms import *
from AppGema.models import Huesped, Reserva, Avatar
from django.views.generic import  ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.views import PasswordChangeView

# Create your views here.

#Vista de inicio y about me

def inicio (request):
    
    return render(request, "AppGema/inicio.html")

def about_me (request):
    
    return render (request, "AppGema/about.html")


# Vistas de registro/login/logout

def registro (request):
    
    if request.method =="POST":
        
        form = UsuarioRegistro(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data["username"]
            form.save()
            return render (request,"AppGema/inicio.html", {"mensaje": "Usuario creado"})
        
    else:
        
        form = UsuarioRegistro()
        
    return render(request, "AppGema/registro/registro.html", {"formulario":form})    



def inicio_sesion (request):
    
    if request.method =="POST":
        
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password = contra)
            
            if user:
                
                login(request, user)
                
                return render(request, "AppGema/inicio.html", {"mensaje":f"Bienvenido  {user}"})
            
        else:
            
            return render(request, "AppGema/inicio.html", {"mensaje": "Datos incorrectos."})    

    else:
                
        form  = AuthenticationForm()    

    return render(request, "AppGema/registro/login.html", {"formulario": form})


def cerrar_sesion(request):
    
    logout(request)
    
    return render(request, "AppGema/inicio.html", {"mensaje": "Hasta pronto!"})


# Vista de editar el perfil

@login_required
def editar_perfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = EditarUsuario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "AppGema/inicio.html")

    else:

        miFormulario = EditarUsuario(initial={'first_name': usuario.first_name,
                                             'last_name':usuario.last_name, 'email': usuario.email})

    return render(request, "AppGema/editar_usuario.html", {"formulario": miFormulario})


# Cambiar contraseña    
    
class Cambiar_Contra(LoginRequiredMixin, PasswordChangeView):
    template_name = "AppGema/cambiar_contra.html"
    success_url = "/AppGema/"

    
#Vista de agregar avatar

@login_required
def agregar_avatar (request):
    
    if request.method =="POST":
        
        form = AvatarFormulario(request.POST, request.FILES)
        
        
        if form.is_valid():
            
            info = form.cleaned_data
            
            usuario_actual= User.objects.get(username=request.user)
            nuevo_avatar = Avatar (usuario= usuario_actual, imagen=info["imagen"])
            
            nuevo_avatar.save()
            
            return render (request,"AppGema/Inicio.html", {"mensaje": "Has creado tu avatar"})
        
    else:
        
        form = AvatarFormulario()
        
    return render(request, "AppGema/nuevo_avatar.html", {"formulario":form})            




#Vistas de Reservas (basadas en funciones)

@login_required
def reserva (request):
    
    return render(request, "AppGema/reserva.html")



@login_required
def leer_reservas(request):
    
    reservas = Reserva.objects.all()
    
    contexto = {"reservations":reservas}
    
    return render(request,"AppGema/reservas/leer_reservas.html", contexto)

@login_required
def crear_reservas(request):
    
    if request.method == "POST":
        
        miFormulario = ReservaFormulario(request.POST)
        
        if miFormulario.is_valid():
            
            info = miFormulario.cleaned_data
            
            reserva = Reserva(nombre = info["nombre"],
                              apellido = info["apellido"],
                              checkin = info["checkin"],
                              checkout = info["checkout"]
                              
                              )
                              
            
            reserva.save()
            
            return render(request, "AppGema/inicio.html")
    else:
        miFormulario = ReservaFormulario() 
    
    return render(request, "AppGema/reservas/reservaformulario.html", {"miFormulario": miFormulario})

@login_required
def eliminar_reservas(request, fecha_ingreso):
    
    reserva = Reserva.objects.get(checkin = fecha_ingreso)
    reserva.delete()
    
    reservas = Reserva.objects.all()
    
    contexto = {"reservations": reservas}
    
    return render (request, "AppGema/reservas/leer_reservas.html", contexto)

@login_required
def editar_reservas(request, name):
    reserva = Reserva.objects.get(nombre = name)
    
    if request.method == "POST":
        
        miFormulario = ReservaFormulario(request.POST)
        
        if miFormulario.is_valid():
            
            info = miFormulario.cleaned_data
            reserva.nombre = info["nombre"],
            reserva.apellido = info["apellido"],
            reserva.checkin = info["checkin"]
            reserva.checkout = info["checkout"]
                              
            reserva.save()
            
            return render(request, "AppGema/inicio.html")
    else:
        miFormulario = ReservaFormulario(initial={"ingreso": reserva.checkin, "egreso": reserva.checkout}) 
    
    return render(request, "AppGema/reservas/editar_reservas.html", {"miFormulario": miFormulario, "nombre": name})

# Vistas de Huesped (basadas en clases)
            
class Lista_Huesped(LoginRequiredMixin,ListView):
    template_name = "AppGema/huespedes/huesped_list.html"
    model = Huesped
    
class Detalle_Huesped(LoginRequiredMixin, DetailView):
    
    template_name = "AppGema/huespedes/huesped_detail.html"
    model = Huesped
    
class Crear_Huesped(LoginRequiredMixin, CreateView):
    
    model = Huesped
    template_name = "AppGema/huespedes/huesped_form.html"
    success_url = "/AppGema/huesped/list"
    fields = ["nombre","apellido","correo"]
    
class Actualizar_Huesped (LoginRequiredMixin, UpdateView):
    
    model = Huesped
    template_name = "AppGema/huespedes/huesped_form.html"
    success_url = "/AppGema/huesped/list"
    fields = ["nombre","apellido","correo"]
    
class Borrar_Huesped(LoginRequiredMixin, DeleteView):
    
    model = Huesped
    template_name = "AppGema/huespedes/huesped_confirm_delete.html"
    success_url = "/AppGema/huesped/list"

# Vistas de habitacion (basadas en clases)

class Lista_Habitacion(ListView):
    
    model = Habitacion
    template_name = "AppGema/habitaciones/habitacion_list.html"
    
class Detalle_Habitacion(DetailView):
    
    model = Habitacion
    template_name = "AppGema/habitaciones/habitacion_detail.html"
    
class Crear_Habitacion(LoginRequiredMixin, CreateView):
    
    model = Habitacion
    template_name = "AppGema/habitaciones/habitacion_form.html"
    success_url = "/AppGema/habitacion/list"
    fields = ["nombre","camas",]
    
class Actualizar_Habitacion (LoginRequiredMixin, UpdateView):
    
    model = Habitacion
    template_name = "AppGema/habitaciones/habitacion_form.html"
    success_url = "/AppGema/habitacion/list"
    fields = ["nombre","camas"]
    
class Borrar_Habitacion(LoginRequiredMixin, DeleteView):
    
    model = Habitacion
    template_name = "AppGema/habitaciones/habitacion_confirm_delete.html"
    success_url = "/AppGema/habitacion/list"
    

    

        


    


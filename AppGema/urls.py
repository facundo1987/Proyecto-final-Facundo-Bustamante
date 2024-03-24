from django.urls import path
from AppGema.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    #URL de inicio y about me 
    path ("", inicio, name = "Inicio"),
    path("about", about_me, name = "Acerca de mi"),
    
    #URLS de registro
    path("login/", inicio_sesion, name="Login"),
    path("register/", registro, name="SignUp"),
    path("logout/", cerrar_sesion, name = "Cerrar_sesion"),
    path("edit/", editar_perfil, name= "Editar usuario"),
    path("contra/", Cambiar_Contra.as_view(), name = "Cambiar Contraseña"),
    
    #URL de avatar
    path("avatar/", agregar_avatar, name= "Agregar Avatar"),
    
    #CRUD de reservas
    
    path("leer_reservas/", leer_reservas, name="Reservas_leer"),
    path("crear_reservas/", crear_reservas, name="Reservas_crear"),
    path("eliminar_reservas/<nombre>/", eliminar_reservas, name = "Reservas_eliminar"),
    path("editar_reservas/<nombre>/", editar_reservas, name = "Reservas_editar"),
    
    #CRUD de huesped 
    
    path("huesped/list",Lista_Huesped.as_view(), name= "Huespedes_Leer"),
    path("huesped/<int:pk>",Detalle_Huesped.as_view(), name= "Huespedes_Detalle"),
    path("huesped/crear/",Crear_Huesped.as_view(), name= "Huespedes_Crear"),
    path("huesped/editar/<int:pk>",Actualizar_Huesped.as_view(), name= "Huespedes_Editar"),
    path("huesped/borrar/<int:pk>", Borrar_Huesped.as_view(), name= "Huespedes_Borrar"),
    
    #CRUD de habitacion 
    
    path("habitacion/list",Lista_Habitacion.as_view(), name= "Habitaciones_Leer"),
    path("habitacion/<int:pk>",Detalle_Habitacion.as_view(), name= "Habitaciones_Detalle"),
    path("habitacion/crear/",Crear_Habitacion.as_view(), name= "Habitaciones_Crear"),
    path("habitacion/editar/<int:pk>",Actualizar_Habitacion.as_view(), name= "Habitaciones_Editar"),
    path("habitacion/borrar/<int:pk>", Borrar_Habitacion.as_view(), name= "Habitaciones_Borrar"),
    
]
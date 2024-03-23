from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Habitacion (models.Model):
    
    nombre = models.CharField(max_length = 60)
    camas = models.IntegerField()
    
    def __str__ (self):
        
        return f"habitacion tipo {self.nombre} ------- contiene {self.camas} cama/s"

class Huesped (models.Model):
    
    nombre = models.CharField(max_length = 60)
    apellido = models.CharField(max_length = 60)
    correo = models.EmailField()
    
    def __str__(self):
        
        return f"{self.nombre} --- {self.apellido}."
    
class Reserva (models.Model):
    
    nombre = models.CharField(max_length = 60,null= True, blank= True, default = None)
    apellido = models.CharField(max_length = 60,null= True, blank= True, default= None)
    checkin = models.DateField()
    checkout = models.DateField()
    
    
    
    def __str__(self):
        
        return f"reserva a nombre de {self.nombre} con ingreso el  {self.checkin}"
    
    
class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to= "avatares", null= True, blank=True)
    
    def __str__(self):
        
        return f"{self.usuario} --- {self.imagen}"
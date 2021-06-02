from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField 
import datetime


# Create your models here.



class tipo_poliza(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='tipo_poliza'
        verbose_name_plural='tipo_polizas'

    
    def __str__(self):

        return self.nombre

class registro(models.Model):
    nombre=models.CharField(max_length=50)
    clave_nueva=models.CharField(max_length=50)
    tipo=models.ForeignKey(tipo_poliza, on_delete=models.CASCADE)
    fecha=models.DateField()
    fecha_termino=models.DateField()
    telefono=models.CharField(max_length=12)
    email=models.EmailField()
    documento=models.FileField(upload_to='documents/')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='registro'
        verbose_name_plural='registros'

    
    def __str__(self):

        return self.nombre

from django.db import models



class Usuario(models.Model):
    nombre=models.CharField(max_length=50, null=False)
    correo=models.EmailField()
    password=models.CharField(max_length=50, blank=False, null=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'

    
    def __str__(self):

        return self.correo



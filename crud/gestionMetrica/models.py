from django.db import models

# Create your models here.
class criteriomedida(models.Model):
    codigo=models.CharField(max_length=3,primary_key=True,serialize=False)
    nombre=models.CharField(max_length=100 )
    descripcion=models.CharField(max_length=1000)
    peso=models.PositiveSmallIntegerField()
    
    def __str__(self):
        texto="{0} ({1})"
        return texto.format(self.nombre, self.descripcion,self.peso)
    

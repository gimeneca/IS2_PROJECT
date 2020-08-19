from django.db import models

# Create your models here.
class proyecto(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=4 , unique=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado_proyecto = (
        ('PEN', 'PENDIENTE'),
        ('TER', 'TERMINADO'),
        ('CUR', 'CURSO'),
    )
    estado = models.CharField(max_length=3, choices=estado_proyecto)
    Sprint = models.CharField(max_length=50) 
    tarea = models.CharField(max_length=50)
    cliente = models.CharField(max_length=50)

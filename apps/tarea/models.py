from django.db import models

# Create your models here.
class tarea(models.Model):
    version = models.CharField(max_length=50)
    prioridad = models.CharField(max_length=50)
    estado_tarea = (
        ('PEN', 'PENDIENTE'),
        ('FIN', 'FINALIZADO'),
        ('INI', 'INICIADO'),
    )
    estado = models.CharField(max_length=3, choices=estado_tarea )
    descripcion = models.CharField(max_length=50)
    observacion = models.CharField(max_length=50)
    id_tarea_padre = models.IntegerField(default=0)
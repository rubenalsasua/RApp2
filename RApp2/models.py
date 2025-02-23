from django.db import models
from django.contrib.auth.models import User


class Etiqueta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='etiquetas', default=1)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Proyecto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='proyectos', default=1)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    fecha_limite = models.DateTimeField(blank=True, null=True)
    PRIORIDAD = [
        ('BAJA', 'Baja'),
        ('MEDIA', 'Media'),
        ('ALTA', 'Alta'),
    ]
    ESTADO = [
        ('SIN_EMPEZAR', 'Sin Empezar'),
        ('EN_PROGRESO', 'En Progreso'),
        ('FINALIZADO', 'Finalizado'),
    ]
    prioridad = models.CharField(max_length=20, choices=PRIORIDAD, default='MEDIA')
    estado = models.CharField(max_length=20, choices=ESTADO, default='SIN_EMPEZAR')
    etiqueta = models.ManyToManyField(Etiqueta, related_name='etiquetas')

    def __str__(self):
        return self.nombre

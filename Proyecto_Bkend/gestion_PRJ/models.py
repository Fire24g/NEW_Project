from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    Encargado_proyecto = models.CharField(max_length=100)
    correo = models.EmailField(max_length=50)
    proyecto_asignado = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.proyecto_asignado}"
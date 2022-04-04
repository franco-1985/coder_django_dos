from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    identificacion = models.IntegerField()

    def __str__(self):
        return self.identificacion + ' - ' + self.nombre + ' - ' + self.fecha_nacimiento

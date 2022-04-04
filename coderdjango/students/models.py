from django.db import models


class Curso(models.Model):
    name = models.CharField(max_length=40)
    camada = models.IntegerField()


class Estudiante(models.Model):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email = models.EmailField()


class Profesor(models.Model):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email = models.EmailField()
    place = models.CharField(max_length=40)


class Entregable(models.Model):
    name = models.CharField(max_length=40)
    end_date = models.DateField()
    sent = models.BooleanField()

class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    identificacion = models.IntegerField()

    def __str__(self):
        return self.identificacion + ' - ' + self.nombre + ' - ' + self.fecha_nacimiento

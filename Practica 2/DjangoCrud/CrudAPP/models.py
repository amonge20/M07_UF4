from django.db import models

# Create your models here.
class Rol(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Person(models.Model):
    nom = models.CharField(max_length=100)
    cognom = models.CharField(max_length=100)
    assignatura = models.CharField(max_length=100)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.nom} {self.cognom}"

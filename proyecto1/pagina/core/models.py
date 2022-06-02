from django.db import models

# Create your models here.
class Concepto(models.Model):
    idConcepto = models.IntegerField(primary_key=True)
    nombreConcepto = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreConcepto

class Obra(models.Model):
    autor = models.CharField(max_length=50, primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    historia = models.CharField(max_length=50)
    tecnica = models.CharField(max_length=50)
    precio = models.IntegerField()
    imagen = models.CharField(max_length=500)
    concepto = models.ForeignKey(Concepto, on_delete=models.CASCADE)

    def __str__(self):
        return self.autor
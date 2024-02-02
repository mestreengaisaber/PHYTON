from django.db import models
from datetime import datetime

# Create your models here.

class FormFactura(models.Model):
	numero = models.CharField(max_length=30, null=False, unique=True, verbose_name="Número")
	importe = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name="Importe")
	fecha = models.DateTimeField(default=datetime.now, null=True, blank=True, verbose_name="Fecha")
	cliente = models.CharField(max_length=200, null=False, verbose_name="Cliente")
	observacion = models.TextField(null=True, blank=True, verbose_name="Observación")
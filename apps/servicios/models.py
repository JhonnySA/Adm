# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from ..reusables.models import Grupo, SubNivel
from ..inicio.models import Estudiante, Institucion, Docente


class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    unidad = models.CharField(max_length=200)

    def __unicode__(self):
        return 'SER: ' + self.nombre

    def get_absolute_url(self):
        return ''


class Matricula(models.Model):
    fechamatricula = models.DateField()
    fechainicio = models.DateField()
    fechafin = models.DateField()
    montototal = models.FloatField()
    descuento = models.FloatField()
    numcuota = models.PositiveIntegerField()
    tipopago = models.CharField(max_length=50)
    conceptodescuento = models.CharField(max_length=200)
    grado = models.CharField(max_length=1)
    observacion = models.CharField(max_length=200)

    estudiante = models.ForeignKey(Estudiante, on_delete=models.PROTECT)
    servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT)
    institucion = models.ForeignKey(Institucion, on_delete=models.PROTECT)
    grupo = models.ForeignKey(Grupo, on_delete=models.PROTECT)

    def __unicode__(self):
        return 'MAT: ' + self.estudiante.nombre + ' - ' + str(self.fechamatricula)


class ClaseParticular(models.Model):
    lugar = models.CharField(max_length=50)
    nrocontacto = models.CharField(max_length=9, unique=True)
    direccion = models.CharField(max_length=200)
    fechasolicitud = models.DateField()
    fechaclase = models.DateField()
    horainicio = models.TimeField()
    horafin = models.TimeField()
    costohora = models.FloatField()
    descuento = models.FloatField()
    obsevacion = models.CharField(max_length=200)

    estudiante = models.ForeignKey(Estudiante, on_delete=models.PROTECT)
    docente = models.ForeignKey(Docente, on_delete=models.PROTECT)
    servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT)
    subnivel = models.ForeignKey(SubNivel, on_delete=models.PROTECT)

    def __unicode__(self):
        return 'CLA PAR: ' + self.estudiante.nombre + ' - ' + str(self.fechasolicitud)


class Practica(models.Model):
    nrocontacto = models.CharField(max_length=9, unique=True)
    fecharecepcion = models.DateField()
    fechaentrega = models.DateField()
    observacion = models.CharField(max_length=200)

    estudiante = models.ForeignKey(Estudiante, on_delete=models.PROTECT)
    servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT)

    def __unicode__(self):
        return 'PRAC' + self.estudiante.nombre + ' - ' + str(self.fecharecepcion)

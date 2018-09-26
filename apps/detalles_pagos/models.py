# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from ..recursos.models import Curso
from ..reusables.models import SubNivel, Grupo
from ..inicio.models import Docente
from ..servicios.models import Practica, Matricula


class DetalleCuota(models.Model):
    matricula = models.ForeignKey(Matricula, on_delete=models.PROTECT)
    nrocuota = models.PositiveIntegerField()

    fechaprogramada = models.DateField()
    fechapago = models.DateField()
    montoprogramado = models.FloatField()
    montopagado = models.FloatField()
    estado = models.BooleanField()

    def __unicode__(self):
        return 'DET CUO: ' + self.matricula_id + ' - ' + self.nroCuota + ' /EST/ ' + self.estado

    class Meta:
        unique_together = (('matricula', 'nrocuota'),)


class DetallePractica(models.Model):
    numejercicio = models.PositiveIntegerField()
    costo = models.FloatField()
    observacion = models.CharField(max_length=200)

    practica = models.ForeignKey(Practica, on_delete=models.PROTECT)
    docente = models.ForeignKey(Docente, on_delete=models.PROTECT)
    subnivel = models.ForeignKey(SubNivel, on_delete=models.PROTECT)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)

    def __unicode__(self):
        return 'DET PRA: ' + self.practica_id + ' - ' + ' /COSTO/ ' + self.costo


class GrupoDocente(models.Model):
    fechainicio = models.DateField()
    fechafin = models.DateField()
    observacion = models.CharField(max_length=200)

    docente = models.ForeignKey(Docente, on_delete=models.PROTECT)
    grupo = models.ForeignKey(Grupo, on_delete=models.PROTECT)

    def __unicode__(self):
        return 'GRU DOC: ' + self.docente.nombre + ' - ' + self.grupo_id + ' \n/TEMPORADA/ ' + str(self.fechafin) + str(
            self.fechafin)

    def EstadoGrupoDocente(self):
        if self.fechafin == None:
            return 'Docente esta activo en el grupo: ' + self.grupo_id

        else:
            return 'Docente ha culminado su temporada en el grupo: ' + self.grupo_id


class DetalleGrupoDocente(models.Model):
    grupodocente = models.ForeignKey(GrupoDocente, on_delete=models.PROTECT)
    nropago = models.PositiveIntegerField()

    nroestudiante = models.PositiveIntegerField()
    mes = models.CharField(max_length=25)
    anio = models.PositiveIntegerField()
    fechapago = models.DateField()
    monto = models.FloatField()
    estado = models.BooleanField()

    def __unicode__(self):
        return 'PAG DOC: ' + self.grupodocente.docente.nombre + ' - ' + self.monto

    def EstadoPagoDocente(self):
        if self.fechapago == None:
            return 'Pago pendiente a Docente: ' + self.grupodocente.docente.nombre

        else:
            return 'Pago cancelado a Docente'

    class Meta:
        unique_together = (('grupodocente', 'nropago'),)

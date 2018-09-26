# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from ..recursos.models import Nivel, Aula


class SubNivel(models.Model):
    rango = models.CharField(max_length=25)
    nivel = models.ForeignKey(Nivel, on_delete=models.PROTECT)

    def __unicode__(self):
        return self.rango


class Dia(models.Model):
    dia1 = models.CharField(max_length=25)
    dia2 = models.CharField(max_length=25)
    dia3 = models.CharField(max_length=25)

    def __unicode__(self):
        return self.dia1 + ' - ' + self.dia2 + ' - ' + self.dia3


class Grupo(models.Model):
    horainicio = models.TimeField()
    horafin = models.TimeField()

    aula = models.ForeignKey(Aula, on_delete=models.PROTECT)
    dia = models.ForeignKey(Dia, on_delete=models.PROTECT)
    subnivel = models.ForeignKey(SubNivel, on_delete=models.PROTECT)

    def __unicode__(self):
        return self.id + ' : ' + str(self.horainicio) + ' - ' + str(self.horafin)

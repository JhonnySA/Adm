# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre


class Aula(models.Model):
    descripcion = models.CharField(max_length=200)
    maxgrupo = models.PositiveIntegerField()

    def __unicode__(self):
        return self.descripcion


class Nivel(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

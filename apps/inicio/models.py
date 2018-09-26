# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class upperCharField(models.CharField):
    def __init__(self, *args, **kwargs):
        self.mayusculas = kwargs.pop("mayusculas", False)
        super(upperCharField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        value = super(upperCharField, self).get_prep_value(value)
        if self.mayusculas:
            return value.upper()
        return value


PersonaSexos = (
    ('M', 'Masculino'),
    ('F', 'Femenino')
)


class Persona(models.Model):
    dni = models.CharField(max_length=8, unique=True)
    paterno = upperCharField(max_length=45, mayusculas=True)
    materno = upperCharField(max_length=45, mayusculas=True)
    nombre = upperCharField(max_length=50, mayusculas=True)
    fechanacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices=PersonaSexos)
    foto = models.ImageField(null=True, blank=True)
    telefono = models.CharField(null=True, blank=True, max_length=8)
    celular = models.CharField(null=True, blank=True, max_length=9)
    correo = models.EmailField(null=True, blank=True, max_length=200)
    direccion = models.CharField(null=True, blank=True, max_length=200)

    def __unicode__(self):
        return self.paterno + ' ' + self.paterno + ' ; ' + self.nombre

    def get_absolute_url(self):
        return ''


class Apoderado(models.Model):
    ocupacion = models.CharField(max_length=100, null=True, blank=True)
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)

    def __unicode__(self):
        return self.persona.nombre

    def get_absolute_url(self):
        return ''


class Estudiante(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT, related_name="persona")
    apoderado = models.ForeignKey(Apoderado, on_delete=models.PROTECT, related_name="apoderado", null=True, blank=True)
    observacion = models.CharField(max_length=200)

    # class Meta:
    #     unique_together = (('persona', 'apoderado'),)

    def __unicode__(self):
        return 'EST: ' + self.persona.paterno + ' ' + self.persona.materno + ' ; ' + self.persona.nombre

    def get_absolute_url(self):
        return ''

    class Meta:
        ordering = ['-id']

    def SexoEstudiante(self):
        return self.persona.sexo

    def NroContacto(self):
        _telefono = ''
        _celular = ''

        if self.apoderado == None:
            return ''
        if self.apoderado.persona.telefono:
            _telefono += str(self.apoderado.persona.telefono)
        if self.apoderado.persona.celular:
            _celular += str(self.apoderado.persona.celular)
        return '%s/%s' % (
            _telefono,
            _celular
        )

    def NombreApoderado(self):
        if self.apoderado == None:
            return ''
        else:
            return '%s %s; %s' % (
                self.apoderado.persona.paterno,
                self.apoderado.persona.materno,
                self.apoderado.persona.nombre
            )


class Docente(models.Model):
    profesion = models.CharField(max_length=100)
    gradoacademico = models.CharField(max_length=100)
    observacion = models.CharField(max_length=200)
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT)

    def __unicode__(self):
        return 'DOC: ' + self.persona.nombre

    def get_absolute_url(self):
        return ''


class Institucion(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=200)

    def __unicode__(self):
        return 'INS: ' + self.nombre

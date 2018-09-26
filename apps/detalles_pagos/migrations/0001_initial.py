# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-15 17:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('servicios', '0001_initial'),
        ('inicio', '0001_initial'),
        ('recursos', '0001_initial'),
        ('reusables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleCuota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nrocuota', models.PositiveIntegerField()),
                ('fechaprogramada', models.DateField()),
                ('fechapago', models.DateField()),
                ('montoprogramado', models.FloatField()),
                ('montopagado', models.FloatField()),
                ('estado', models.BooleanField()),
                ('matricula', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='servicios.Matricula')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleGrupoDocente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nropago', models.PositiveIntegerField()),
                ('nroestudiante', models.PositiveIntegerField()),
                ('mes', models.CharField(max_length=25)),
                ('anio', models.PositiveIntegerField()),
                ('fechapago', models.DateField()),
                ('monto', models.FloatField()),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='DetallePractica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numejercicio', models.PositiveIntegerField()),
                ('costo', models.FloatField()),
                ('observacion', models.CharField(max_length=200)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recursos.Curso')),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inicio.Docente')),
                ('practica', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='servicios.Practica')),
                ('subnivel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reusables.SubNivel')),
            ],
        ),
        migrations.CreateModel(
            name='GrupoDocente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechainicio', models.DateField()),
                ('fechafin', models.DateField()),
                ('observacion', models.CharField(max_length=200)),
                ('docente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inicio.Docente')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reusables.Grupo')),
            ],
        ),
        migrations.AddField(
            model_name='detallegrupodocente',
            name='grupodocente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='detalles_pagos.GrupoDocente'),
        ),
        migrations.AlterUniqueTogether(
            name='detallegrupodocente',
            unique_together=set([('grupodocente', 'nropago')]),
        ),
        migrations.AlterUniqueTogether(
            name='detallecuota',
            unique_together=set([('matricula', 'nrocuota')]),
        ),
    ]

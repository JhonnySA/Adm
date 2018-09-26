from django.urls import reverse
from django.utils.html import format_html

from ..table.columns import Column
from ..models import Docente
from ..tables_inicio.table_default import TablaDefault


class Acciones(Column):
    def render(self, obj):
        _result = ''

        urlEditar = reverse(viewname="inicio:docente_editar", kwargs={'pk': obj.pk})
        _result += "<button type='button' class='btn btn-xs btn-primary' title='Editar' href='" + urlEditar + "' data-toggle='modal' data-target='#modalMaestro'><i class='fa fa-pencil'></i></button>&nbsp;"

        urlEliminar = reverse(viewname="inicio:docente_eliminar", kwargs={'pk': obj.pk})
        _result += "<button type='button' class='btn btn-xs btn-primary' title='Eliminar' href='" + urlEliminar + "' data-toggle='modal' data-target='#modalMaestro'><i class='fa fa-trash'></i></button>&nbsp;"
        return _result


class NombreColumn(Column):
    def render(self, obj):
        return "%s %s %s" % (
            obj.persona.paterno,
            obj.persona.materno,
            obj.persona.nombre
        )


class TablaDocente(TablaDefault):
    dni = Column(field='persona.dni', header='DNI')
    nombres = NombreColumn(field='persona.dni', header='Paterno', searchable=False, sortable=False)
    paterno = Column(field='persona.paterno', header='Paterno', visible=False)
    materno = Column(field='persona.materno', header='Materno', visible=False)
    nombre = Column(field='persona.nombre', header='Nombre(s)', visible=False)
    celular = Column(field='persona.celular', header='Celular')
    gradoacademico = Column(field='gradoacademico', header='Grado Academico')
    profesion = Column(field='profesion', header='Profesion')
    acciones = Acciones(field='pk', header='Acciones')

    class Meta(TablaDefault.Meta):
        model = Docente
        id = 'tablaDocente'
        # urlAgregar = '<button type="button" class="btn btn-sm btn-primary" data-toggle="modal" data-target="#modalMaestro" href="' + to_url + '"><span class="fa fa-plus-circle" aria-hidden="true"></span> Agregar</button>'
        # ajax_source = ''

    def __init__(self):
        super(TablaDocente, self).__init__()
        self.opts.buttons = [
            {'texto': 'Agregar', 'icono': 'fa fa-plus', 'url': reverse(viewname="inicio:docente_agregar")}
        ]

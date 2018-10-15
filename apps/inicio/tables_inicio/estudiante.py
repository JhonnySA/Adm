# coding=utf-8
from django.urls import reverse
from ..table.columns import Column

from ..models import Estudiante
from ..tables_inicio.table_default import TablaDefault


class NombreEstudiante(Column):
    def render(self, obj):
        return '%s %s; %s' % (
            obj.persona.paterno,
            obj.persona.materno,
            obj.persona.nombre
        )


class SexoEstudiante(Column):
    def render(self, obj):
        if obj.SexoEstudiante() == 'M':
            return '<p class="text-center text-info"><i class="fa fa-male"></i></p>'
        else:
            return '<p class="text-center text-danger"><i class="fa fa-female"></i></p>'


class NroContacto(Column):
    def render(self, obj):
        _result = ''
        _telefono = ''
        _celular = ''

        contacto = obj.NroContacto().split('/')
        if len(contacto) == 2:
            if not contacto[0] == '':
                _result += '<span><i class="fa fa-phone text-info text-bold"></i> ' + contacto[
                    0] + ' </span>&nbsp;'
            if not contacto[1] == '':
                _result += '<span><i class="fa fa-mobile-phone text-info text-bold"></i> ' + contacto[
                    1] + '</span>'
            return _result
        else:
            return '<p class="text-center">--------</p>'


class NombreApoderado(Column):
    def render(self, obj):
        _icono = ''
        _button = ''
        # urlAgregarApoderado = reverse(viewname='inicio:apoderado_agregar', kwargs={"estudiante": obj.pk})
        urlApoderado = None

        if obj.NombreApoderado() == '':
            urlApoderado = reverse(viewname='inicio:apoderado_agregar', kwargs={"estudiante": obj.pk})
            _result = '<span class="pull-left"><code><i class="icon fa fa-warning"></i>Ninguno</code></span>'
            _button = 'btn btn-xs btn-danger pull-right'
            _icono = 'fa fa-plus'
        else:
            urlApoderado = reverse(viewname='inicio:apoderado_editar', kwargs={"pk": obj.pk})
            _result = obj.NombreApoderado()
            _button = 'btn btn-xs btn-success pull-right'
            _icono = 'fa fa-pencil'
        _result += "<button type='button' class='" + _button + "' title='Apoderado' href='" + urlApoderado + "' data-toggle='modal' data-target='#modalMaestro'><i class='" + _icono + "'></i></button>"
        return _result


class Direccion(Column):
    def render(self, obj):
        if obj.persona.direccion == None:
            return '<p class="text-center">--------</p>'
        else:
            return obj.persona.direccion


class Acciones(Column):
    def render(self, obj):
        _result = ''
        urlEditar = reverse(viewname='inicio:estudiante_editar', kwargs={'pk': obj.pk})
        _result += "<button type='button' class='btn btn-xs btn-primary' title='Editar' href='" + urlEditar + "' data-toggle='modal' data-target='#modalMaestro'><i class='fa fa-pencil'></i></button>&nbsp;"

        _urlEliminar = reverse(viewname='inicio:estudiante_eliminar', kwargs={'pk': obj.pk})
        _result += "<button type='button' class='btn btn-xs btn-danger' title='Eliminar' href='" + _urlEliminar + "' data-toggle='modal' data-target='#modalMaestro'><i class='fa fa-trash'></i></button>&nbsp;"
        return _result


class TablaEstudiante(TablaDefault):
    id = Column(field='pk', header='ID')
    dni = Column(field='persona.dni', header='DNI')
    paterno = Column(field='persona.paterno', header='Paterno', visible=False)
    materno = Column(field='persona.materno', header='Materno', visible=False)
    nombre = Column(field='persona.nombre', header='Nombre', visible=False)
    nombres = NombreEstudiante(field='pk', header='Nombres', searchable=False, sortable=False)
    sexo = SexoEstudiante(field='persona.pk', header='Sexo')
    fechanacimiento = Column(field='persona.fechanacimiento', header='Cumpleaños')
    apoderado = NombreApoderado(field='pk', header='Apoderado', searchable=False, sortable=False)
    nrocontacto = NroContacto(field='persona.pk', header='Contacto')
    direccion = Direccion(field='persona.direccion', header='Direccion')
    acciones = Acciones(field='pk', header='Acciones')

    class Meta(TablaDefault.Meta):
        model = Estudiante
        info_format = 'Estudiantes registrados: ' + '_TOTAL_'
        id = 'tablaEstudiante'
        ajax_source = ''

    def __init__(self):
        super(TablaEstudiante, self).__init__()
        self.opts.buttons = [
            {'texto': 'Agregar', 'icono': 'fa fa-plus', 'url': reverse(viewname='inicio:estudiante_agregar')},
            {'texto': 'Excel', 'icono': 'fa fa-download', 'extend': 'csv'},
            {'texto': 'Pdf', 'icono': 'fa fa-download', 'extend': 'pdf'},
        ]
        print(len(self.opts.buttons))

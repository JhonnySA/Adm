from django.urls import reverse

from ..models import Servicio
from ...inicio.table.columns import Column
from ...inicio.tables_inicio.table_default import TablaDefault


class Acciones(Column):
    def render(self, obj):
        _result = ''
        urlEditar = reverse(viewname='servicio:servicio_editar', kwargs={'pk': obj.pk})
        _result += "<button type='button' class='btn btn-xs btn-primary' title='Editar' href='" + urlEditar + "' data-toggle='modal' data-target='#modalMaestro'><i class='fa fa-pencil'></i></button>&nbsp;"

        urlEliminar = reverse(viewname='servicio:servicio_eliminar', kwargs={'pk': obj.pk})
        _result += "<button type='button' class='btn btn-xs btn-danger' title='Eliminar' href='" + urlEliminar + "' data-toggle='modal' data-target='#modalMaestro'><i class='fa fa-trash'></i></button>&nbsp;"
        return _result


class TablaServicio(TablaDefault):
    id = Column(field='pk', header='ID')
    nombre = Column(field='nombre', header='Nombre')
    descripcion = Column(field='descripcion', header='Descripcion')
    unidad = Column(field='unidad', header='Unidad')
    acciones = Acciones(field='pk', header='Acciones')

    class Meta(TablaDefault.Meta):
        model = Servicio
        info_format = 'Servicios registrados: ' + '_TOTAL_'
        id = 'tablaServicio'
        ajaxSource = ''

    def __init__(self):
        super(TablaServicio, self).__init__()
        self.opts.buttons = [
            {'texto': 'Agregar', 'icono': 'fa fa-plus', 'url': reverse(viewname='servicio:servicio_agregar')}
        ]

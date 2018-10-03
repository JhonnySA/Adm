from django.urls import reverse

from ...inicio.table.columns import Column
from ..models import Grupo
from ...inicio.tables_inicio.table_default import TablaDefault


class Acciones(Column):
    def render(self, obj):
        _result = ''
        urlEditar = reverse(viewname='reusables:grupo_editar', kwargs={'pk': obj.pk})
        _result += "<button type='button' class='btn btn-xs btn-primary' title='Editar' href='" + urlEditar + "' data-toggle='modal' data-target='#modalMaestro'><i class='fa fa-pencil'></i></button>&nbsp;"

        _urlEliminar = reverse(viewname='reusables:grupo_eliminar', kwargs={'pk': obj.pk})
        _result += "<button type='button' class='btn btn-xs btn-danger' title='Eliminar' href='" + _urlEliminar + "' data-toggle='modal' data-target='#modalMaestro'><i class='fa fa-trash'></i></button>&nbsp;"
        return _result


class TablaGrupo(TablaDefault):
    inicio = Column(field='horainicio', header='Inicio')
    fin = Column(field='horafin', header='Fin')
    aula = Column(field='aula', header='Aula')
    dia = Column(field='dia', header='Dias')
    subnivel = Column(field='subnivel', header='SubNivel')
    acciones = Acciones(field='pk', header='Acciones')

    class Meta(TablaDefault.Meta):
        model = Grupo
        id = 'tablaGrupo'
        info_format = 'Grupos registrados: ' + '_TOTAL_'
        ajax_source = ''

    def __init__(self):
        super(TablaGrupo, self).__init__()
        self.opts.buttons = [
            {'texto': 'Agregar', 'icono': 'fa fa-plus', 'url': reverse(viewname='reusables:grupo_agregar')}
        ]

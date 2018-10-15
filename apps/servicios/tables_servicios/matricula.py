from django.urls import reverse

from ...inicio.table.columns import Column
from ..models import Matricula
from ...inicio.tables_inicio.table_default import TablaDefault


class TablaMatricula(TablaDefault):
    id = Column(field='pk', header='ID')

    class Meta(TablaDefault.Meta):
        model = Matricula
        info_format = 'Matriculas registradas:' + ' _TOTAL_'
        id = 'TablaMatricula'
        ajax_source = ''

    def __init__(self):
        super(TablaMatricula, self).__init__()
        self.opts.buttons = [
            {'texto': 'Agregar', 'icono': 'fa fa-plus', 'url': reverse(viewname='servicio:matricula_agregar')}
        ]

from ..table import Table


class TablaDefault(Table):
    class Meta:
        ajax = True
        attrs = {
            "style": 'background-color: #fff; width: 100%',
            "class": 'table-striped table-hover dt-responsive',
            "width": '100%'
        }
        pagination = True
        pagination_firts = "<<"
        pagination_prev = "<"
        pagination_next = ">"
        pagination_last = ">>"
        search_placeholder = "Buscar..."
        zero_records = "Sin informacion que mostrar"
        rows = "%d Fila Seleccionadas"

# Esta clase se puede mejorar si se recibe parametros como URLS opcionales, en caso de recibir un update crea
# el boton UPDATE, etc

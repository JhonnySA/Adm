from django.conf.urls import url

from .views_servicios.servicio import ServicioVista, ServicioAgregar, ServicioEditar, ServicioEliminar
from .views_servicios.servicios import Servicios

urlpatterns = [
    url(r'^$', Servicios.as_view(), name='servicio'),

    url(r'^catalogo/$', ServicioVista.as_view(), name='servicio_vista'),
    url(r'^agregar/$', ServicioAgregar.as_view(), name='servicio_agregar'),
    url(r'^editar/(?P<pk>\d+)$', ServicioEditar.as_view(), name='servicio_editar'),
    url(r'^eliminar/(?P<pk>\d+)$', ServicioEliminar.as_view(), name='servicio_eliminar'),
]

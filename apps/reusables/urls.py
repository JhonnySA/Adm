from django.conf.urls import url

from .view_reusables.grupo import GrupoVista, GrupoAgregar, GrupoEditar, GrupoEliminar
from ..reusables.view_reusables.grupos import Reusables

urlpatterns = [
    url(r'^$', Reusables.as_view(), name='reusables'),

    url(r'^grupo/$', GrupoVista.as_view(), name='grupo_vista'),
    url(r'^grupo/agregar/$', GrupoAgregar.as_view(), name='grupo_agregar'),
    url(r'^grupo/editar/(?P<pk>\d+)$', GrupoEditar.as_view(), name='grupo_editar'),
    url(r'^grupo/eliminar/(?P<pk>\d+)$', GrupoEliminar.as_view(), name='grupo_eliminar'),
]

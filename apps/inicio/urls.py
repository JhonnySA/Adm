from django.conf.urls.static import url

from .views_inicio.docente import DocenteVista, DocenteAgregar, DocenteEditar, DocenteEliminar
from .views_inicio.apoderado import ApoderadoAgregar, ApoderadoActualizar
from .views_inicio.estudiante import EstudianteVista, EstudianteAgregar, EstudianteEditar, EstudianteEliminar
from .views_inicio.persona import PersonaBuscar
from .views_inicio.inicio import Inicio

urlpatterns = [
    # Inicio - Home
    url(r'^$', Inicio.as_view(), name='inicio'),

    # Persona
    url(r'persona/buscar/(?P<dni>\d+)$', PersonaBuscar.as_view(), name='persona_buscar'),

    # Estudiante
    url(r'estudiante/$', EstudianteVista.as_view(), name='estudiante_vista'),
    url(r'estudiante/agregar/$', EstudianteAgregar.as_view(), name='estudiante_agregar'),
    url(r'estudiante/editar/(?P<pk>\d+)$', EstudianteEditar.as_view(), name='estudiante_editar'),
    url(r'estudiante/eliminar/(?P<pk>\d+)$', EstudianteEliminar.as_view(), name='estudiante_eliminar'),

    # Apoderado
    url(r'estudiante/(?P<estudiante>\d+)/agregar/apoderado/$', ApoderadoAgregar.as_view(), name='apoderado_agregar'),
    url(r'estudiante/(?P<estudiante>\d+)/actualizar/apoderado/$', ApoderadoActualizar.as_view(), name='apoderado_actualizar'),

    # Docente
    url(r'docente/$', DocenteVista.as_view(), name='docente_vista'),
    url(r'docente/agregar/$', DocenteAgregar.as_view(), name='docente_agregar'),
    url(r'docente/editar/(?P<pk>\d+)$', DocenteEditar.as_view(), name='docente_editar'),
    url(r'docente/eliminar/(?P<pk>\d+)$', DocenteEliminar.as_view(), name='docente_eliminar'),
]

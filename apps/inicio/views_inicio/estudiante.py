from django.db.models import ProtectedError
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

from ..forms_inicio.estudiante import EstudianteForm
from ..models import Estudiante
from ..tables_inicio.estudiante import TablaEstudiante


class EstudianteVista(TemplateView):
    template_name = 'estudiante/vista.html'

    def render_to_response(self, context, **response_kwargs):
        context['tablaEstudiante'] = TablaEstudiante()
        return super(EstudianteVista, self).render_to_response(context, **response_kwargs)


class EstudianteAgregar(CreateView):
    template_name = "estudiante/agregar.html"
    model = Estudiante
    form_class = EstudianteForm

    def render_to_response(self, context, **response_kwargs):
        context['formEstudiante'] = self.get_form()
        return super(EstudianteAgregar, self).render_to_response(context, **response_kwargs)

    def form_valid(self, form):
        super(EstudianteAgregar, self).form_valid(form)
        msg = {}
        msg["msg"] = "Estudiante creado con exito"
        msg['value'] = True
        return JsonResponse(msg)

    def form_invalid(self, form):
        super(EstudianteAgregar, self).form_invalid(form)
        return render(self.request, self.template_name, {'formEstudiante': form})


class EstudianteEditar(UpdateView):
    template_name = 'estudiante/agregar.html'
    model = Estudiante
    form_class = EstudianteForm

    def render_to_response(self, context, **response_kwargs):
        context['formEstudiante'] = self.get_form()
        return super(EstudianteEditar, self).render_to_response(context, **response_kwargs)

    def form_valid(self, form):
        super(EstudianteEditar, self).form_valid(form)
        msg = {}
        msg['msg'] = 'Estudiante actualizado correctamente'
        msg['value'] = True
        return JsonResponse(msg)

    def form_invalid(self, form):
        super(EstudianteEditar, self).form_invalid(form)
        return render(self.request, self.template_name, {'formEstudiante', form})


class EstudianteEliminar(DeleteView):
    template_name = 'estudiante/eliminar.html'
    model = Estudiante
    form_class = EstudianteForm

    def delete(self, request, *args, **kwargs):
        msg = {}
        msg['msg'] = 'Estudiante eliminado correctamente'
        msg['value'] = True
        try:
            self.get_object().delete()
        except ProtectedError as e:
            msg['value'] = False
            return render(request, self.template_name,
                          {'object': self.get_object(), 'delete_error': 'Este estudiante no puede ser eliminado'})
        except Exception as e:
            msg['value'] = False
            return render(request, self.template_name,
                          {'object': self.get_object(), 'delete_error': str(e)})
        return JsonResponse(msg)

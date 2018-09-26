from django.db.models import ProtectedError
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

from apps.inicio.forms_inicio.docente import DocenteForm
from ..models import Docente
from ..tables_inicio.docente import TablaDocente


class DocenteVista(TemplateView):
    template_name = 'docente/vista.html'

    def render_to_response(self, context, **response_kwargs):
        context['tablaDocente'] = TablaDocente()
        return super(DocenteVista, self).render_to_response(context, **response_kwargs)


class DocenteAgregar(CreateView):
    template_name = 'docente/agregar.html'
    model = Docente
    form_class = DocenteForm

    def render_to_response(self, context, **response_kwargs):
        context['formDocente'] = self.get_form()
        return super(DocenteAgregar, self).render_to_response(context, **response_kwargs)

    def form_valid(self, form):
        super(DocenteAgregar, self).form_valid(form)
        msg = {}
        msg["msg"] = "Docente creado con exito"
        msg['value'] = True
        return JsonResponse(msg)

    def form_invalid(self, form):
        super(DocenteAgregar, self).form_invalid(form)
        return render(self.request, self.template_name, {'formDocente': form})


class DocenteEditar(UpdateView):
    template_name = 'docente/agregar.html'
    model = Docente
    form_class = DocenteForm
    context_object_name = 'uDocente'

    def render_to_response(self, context, **response_kwargs):
        context['formDocente'] = self.get_form()
        return super(DocenteEditar, self).render_to_response(context, **response_kwargs)

    def form_valid(self, form):
        super(DocenteEditar, self).form_valid(form)
        msg = {}
        msg["msg"] = "Docente actualizado correctamente"
        msg["value"] = True
        return JsonResponse(msg)

    def form_invalid(self, form):
        super(DocenteEditar, self).form_invalid(form)
        return render(self.request, self.template_name, {'formDocente': form})


class DocenteEliminar(DeleteView):
    template_name = 'docente/eliminar.html'
    model = Docente
    form_class = DocenteForm

    def delete(self, request, *args, **kwargs):
        msg = {}
        msg['msg'] = 'Docente eliminado correctamente'
        msg['value'] = True
        try:
            self.get_object().delete()
        except ProtectedError as e:
            msg['value'] = False
            return render(request, self.template_name,
                          {'object': self.get_object(), 'delete_error': 'Este registro no puede ser eliminado'})
        except Exception as e:
            msg['value'] = False
            return render(request, self.template_name,
                          {'object': self.get_object(), 'delete_error': str(e)})
        return JsonResponse(msg)

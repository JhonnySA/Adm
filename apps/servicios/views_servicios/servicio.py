from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import ProtectedError
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

from ..forms_servicio.servicio import ServicioForm
from ..models import Servicio
from ..tables_servicios.servicio import TablaServicio


class ServicioVista(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    redirect_field_name = ''
    template_name = 'servicio/vista.html'

    def render_to_response(self, context, **response_kwargs):
        context['tablaServicio'] = TablaServicio()
        return super(ServicioVista, self).render_to_response(context, **response_kwargs)


class ServicioAgregar(CreateView):
    template_name = 'servicio/agregar.html'
    model = Servicio
    form_class = ServicioForm

    def render_to_response(self, context, **response_kwargs):
        context['formServicio'] = self.get_form()
        return super(ServicioAgregar, self).render_to_response(context, **response_kwargs)

    def form_valid(self, form):
        super(ServicioAgregar, self).form_valid(form)
        msg = {}
        msg["msg"] = "Servicio creado con exito"
        msg["value"] = True
        return JsonResponse(msg)

    def form_invalid(self, form):
        super(ServicioAgregar, self).form_invalid(form)
        return render(self.request, self.template_name, {'formServicio': form})


class ServicioEditar(UpdateView):
    template_name = 'servicio/agregar.html'
    model = Servicio
    form_class = ServicioForm

    def render_to_response(self, context, **response_kwargs):
        context['formServicio'] = self.get_form()
        return super(ServicioEditar, self).render_to_response(context, **response_kwargs)

    def form_valid(self, form):
        super(ServicioEditar, self).form_valid(form)
        msg = {}
        msg["msg"] = "Servicio actualizado correctamente"
        msg["value"] = True
        return JsonResponse(msg)

    def form_invalid(self, form):
        super(ServicioEditar, self).form_invalid(form)
        return render(self.request, self.template_name, {'formServicio': form})


class ServicioEliminar(DeleteView):
    template_name = 'servicio/eliminar.html'
    model = Servicio
    form_class = ServicioForm

    def delete(self, request, *args, **kwargs):
        msg = {}
        msg["msg"] = "Servicio eliminado correctamente"
        msg["value"] = True
        try:
            self.get_object().delete()
        except ProtectedError as  e:
            msg["value"] = False
            return render(request, self.template_name,
                          {'object': self.get_object(), 'delete_error': 'Este servicio no puede ser eliminado'})
        except Exception as e:
            msg["value"] = False
            return render(request, self.template_name,
                          {'object': self.get_object(), 'delete_error': str(e)})
        return JsonResponse(msg)

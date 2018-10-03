from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import ProtectedError
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

from ..forms_reusables.grupo import GrupoForm
from ..models import Grupo
from ..tables_reusables.grupo import TablaGrupo


class GrupoVista(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    redirect_field_name = ''
    template_name = 'grupo/vista.html'

    def render_to_response(self, context, **response_kwargs):
        context['tablaGrupo'] = TablaGrupo()
        return super(GrupoVista, self).render_to_response(context, **response_kwargs)


class GrupoAgregar(CreateView):
    template_name = 'grupo/agregar.html'
    model = Grupo
    form_class = GrupoForm

    def render_to_response(self, context, **response_kwargs):
        context['formGrupo'] = self.get_form()
        return super(GrupoAgregar, self).render_to_response(context, **response_kwargs)

    def form_valid(self, form):
        super(GrupoAgregar, self).form_valid(form)
        msg = {}
        msg["msg"] = "Grupo creado con exito"
        msg["value"] = True
        return JsonResponse(msg)

    def form_invalid(self, form):
        super(GrupoAgregar, self).form_invalid(form)
        return render(self.request, self.template_name, {'formGrupo': form})


class GrupoEditar(UpdateView):
    template_name = 'grupo/agregar.html'
    model = Grupo
    form_class = GrupoForm

    def render_to_response(self, context, **response_kwargs):
        context['formGrupo'] = self.get_form()
        return super(GrupoEditar, self).render_to_response(context, **response_kwargs)

    def form_valid(self, form):
        super(GrupoEditar, self).form_valid(form)
        msg = {}
        msg["msg"] = "Grupo actualizado correctamente"
        msg["value"] = True
        return JsonResponse(msg)

    def form_invalid(self, form):
        super(GrupoEditar, self).form_invalid(form)
        return render(self.request, self.template_name, {'formGrupo': form})


class GrupoEliminar(DeleteView):
    template_name = 'grupo/eliminar.html'
    model = Grupo
    form_class = GrupoForm

    def delete(self, request, *args, **kwargs):
        msg = {}
        msg["msg"] = "Grupo eliminado correctamente"
        msg["value"] = True

        try:
            self.get_object().delete()
        except ProtectedError as e:
            msg["value"] = False
            return render(request, self.template_name,
                          {'object': self.get_object()}, {'delete_error': 'Este grupo no puede ser eliminado'})
        except Exception as e:
            msg["value"] = False
            return render(request, self.template_name,
                          {'object': self.get_object()}, {'delete_error': str(e)})
        return JsonResponse(msg)

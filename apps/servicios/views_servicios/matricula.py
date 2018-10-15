from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

from ..forms_servicio.matricula import MatriculaForm
from ..models import Matricula
from ..tables_servicios.matricula import TablaMatricula


class MatriculaVista(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    redirect_field_name = ''
    template_name = 'matricula/vista.html'

    def render_to_response(self, context, **response_kwargs):
        context['tablaMatricula'] = TablaMatricula()
        return super(MatriculaVista, self).render_to_response(context, **response_kwargs)

class MatriculaAgregar(CreateView):
    model = Matricula
    template_name = 'matricula/agregar.html'
    form_class = MatriculaForm
    
    def render_to_response(self, context, **response_kwargs):
        context['formMatricula']=self.get_form()
        return super(MatriculaAgregar, self).render_to_response(context, **response_kwargs)

    def form_valid(self, form):
        super(MatriculaAgregar, self).form_valid(form)
        msg={}
        msg["msg"]="Matricula creada con exito"
        msg["value"]=True
        return JsonResponse(msg)

    def form_invalid(self, form):
        super(MatriculaAgregar, self).form_invalid(form)
        return render(self.request, self.template_name,{'formMatricula': form })
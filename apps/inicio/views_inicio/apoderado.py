from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView

from ..forms_inicio.apoderado import ApoderadoForm
from ..models import Apoderado


class ApoderadoAgregar(CreateView):
    template_name = 'apoderado/agregar.html'
    model = Apoderado
    form_class = ApoderadoForm

    def get_form_kwargs(self):
        data = super(ApoderadoAgregar, self).get_form_kwargs()
        data["kwargs"] = self.kwargs
        return data

    def render_to_response(self, context, **response_kwargs):
        context['formApoderado'] = self.get_form()
        return super(ApoderadoAgregar, self).render_to_response(context, **response_kwargs)

    def form_valid(self, form):
        super(ApoderadoAgregar, self).form_valid(form)
        msg = {}
        msg["msg"] = "Apoderado agregado correctamente"
        msg['value'] = True
        return JsonResponse(msg)

    def form_invalid(self, form):
        super(ApoderadoAgregar, self).form_invalid(form)
        return render(self.request, self.template_name, {'formApoderado': form})


class ApoderadoActualizar(UpdateView):
    template_name = 'apoderado/agregar.html'
    model = Apoderado
    form_class = ApoderadoForm

    def get_form_kwargs(self):
        data = super(ApoderadoActualizar, self).get_form_kwargs()
        data["kwargs"] = self.kwargs
        return data

    def render_to_response(self, context, **response_kwargs):
        context['formApoderado'] = self.get_form()
        return super(ApoderadoActualizar, self).render_to_response(context, **response_kwargs)

    def form_valid(self, form):
        super(ApoderadoActualizar, self).form_valid(form)
        msg = {}
        msg['msg'] = 'Apoderado actualizado correctamente'
        msg['value'] = True
        return JsonResponse(msg)

    def form_invalid(self, form):
        super(ApoderadoActualizar, self).form_invalid(form)
        return render(self.request, self.template_name, {'formApoderado': form})

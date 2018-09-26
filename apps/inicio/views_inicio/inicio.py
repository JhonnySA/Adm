from django.views.generic import TemplateView


class Inicio(TemplateView):
    template_name = 'inicio/inicio.html'
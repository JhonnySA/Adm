from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class Inicio(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    redirect_field_name = ''
    template_name = 'inicio/inicio.html'

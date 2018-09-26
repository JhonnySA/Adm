from django.views.generic import TemplateView

from apps.inicio.models import Persona


class PersonaBuscar(TemplateView):
    template_name = 'persona/buscar.json'
    http_method_names = 'post'
    content_type = 'application/json'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["persona"] = Persona.objects.filter(
            dni=self.kwargs.get('dni')
        ).first()
        return self.render_to_response(context=context)

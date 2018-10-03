from datetimewidget.widgets import TimeWidget
from django import forms
from django_select2.forms import ModelSelect2Widget

from ..models import Aula, Dia, SubNivel
from ...reusables.models import Grupo


class TimeInput(forms.TimeInput):
    template_name = 'campos/time.html'


class SubnivelWidget(ModelSelect2Widget):
    queryset = SubNivel.objects.all()
    search_fields = ['rango__icontains']

    def label_from_instance(self, obj):
        return '(%s) - %s' % (
            obj.rango,
            obj.nivel.nombre
        )


class GrupoForm(forms.ModelForm):
    horainicio = forms.TimeField(
        label='Hora inicio',
        required=True,
        widget=TimeWidget()
    )

    horafin = forms.CharField(
        label='Hora fin',
        required=True,
        widget=TimeWidget()
    )

    aula = forms.ModelChoiceField(
        required=True,
        queryset=Aula.objects.all(),
        label='Aula',
        widget=ModelSelect2Widget(
            queryset=Aula.objects.order_by('id'),
            search_fields=['descripcion__icontains'],
            max_results=5
        )
    )

    dia = forms.ModelChoiceField(
        required=True,
        queryset=Dia.objects.all(),
        label='Dias',
        widget=ModelSelect2Widget(
            queryset=Dia.objects.order_by('id'),
            search_fields=[
                'dia1__icontains',
                'dia2__icontains',
                'dia3__icontains'],
            max_results=5
        )
    )

    subnivel = forms.ModelChoiceField(
        required=True,
        queryset=SubNivel.objects.all(),
        label='Subnivel',
        widget=SubnivelWidget()
    )

    def __init__(self, *args, **kwargs):
        super(GrupoForm, self).__init__(*args, **kwargs)
        for i, (fname, field) in enumerate(self.fields.iteritems()):
            field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' form-control'

    class Meta:
        model = Grupo
        fields = ['horainicio', 'horafin', 'aula', 'dia', 'subnivel']

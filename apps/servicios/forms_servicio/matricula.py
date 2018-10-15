# coding=utf-8
from datetimewidget.widgets import DateWidget
from django import forms
from django_select2.forms import ModelSelect2Widget

from ...reusables.models import Grupo
from ...inicio.models import Institucion
from ...recursos.models import Nivel
from ..models import Estudiante, Matricula, Turno, TipoPago
from ..models import Servicio


class MatriculaForm(forms.ModelForm):
    servicio = forms.ModelChoiceField(
        required=True,
        queryset=Servicio.objects.all(),
        label='Servicio',
        widget=ModelSelect2Widget(
            queryset=Servicio.objects.all(),
            search_fields=['nombre__icontains']
        )
    )

    estudiante = forms.ModelChoiceField(
        required=True,
        queryset=Estudiante.objects.all(),
        label='Estudiante',
        widget=ModelSelect2Widget(
            queryset=Estudiante.objects.all(),
            search_fields=['nombre__icontains'],
            max_results=10
        )
    )

    nivel = forms.ModelChoiceField(
        required=False,
        queryset=Nivel.objects.all(),
        label='Nivel',
        widget=ModelSelect2Widget(
            queryset=Nivel.objects.all(),
            search_fields=['nombre__icontains']
        )
    )

    grado = forms.CharField(
        label='Grado',
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Grado'})
    )

    institucion = forms.ModelChoiceField(
        required=False,
        queryset=Institucion.objects.all(),
        label='Institucion',
        widget=ModelSelect2Widget(
            queryset=Institucion.objects.all(),
            search_fields=['nombre__icontains']
        )
    )

    turno = forms.ChoiceField(choices=Turno)

    grupo = forms.ModelChoiceField(
        required=True,
        queryset=Grupo.objects.all(),
        label='Grupo',
        widget=ModelSelect2Widget(
            queryset=Grupo.objects.all(),
            search_fields=[''],
            max_results=5
        )
    )

    observacion = forms.CharField(
        label='Observacion',
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Alguna obsevacion'})
    )

    fechainicio = forms.DateField(
        label='Fecha de inicio',
        input_formats=["%d/%m/%Y"],
        widget=DateWidget(
            attrs={"data-datepicker-type": "4", "data-provider": "datepicker-inline"},
            bootstrap_version=3,
            options={
                "format": "dd/mm/yyyy",
                "autoclose": "true",
                "language": "es",
                "fontAwesome": "true",
                "clearBtn": "false"
            }
        )
    )

    fechafin = forms.DateField(
        label='Fecha de fin',
        input_formats=["%d/%m/%Y"],
        widget=DateWidget(
            attrs={"data-datepicker-type": "4", "data-provider": "datepicker-inline"},
            bootstrap_version=3,
            options={
                "format": "dd/mm/yyyy",
                "autoclose": "true",
                "language": "es",
                "fontAwesome": "true",
                "clearBtn": "false"
            }
        )
    )

    tipopago = forms.ChoiceField(choices=TipoPago)

    descuento = forms.FloatField(
        label='Descuento',
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': 'Descuento'})
    )

    conceptodescuento = forms.CharField(
        label='Motivo de descuento',
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Motivo de descuento',
                'cols': 30, 'rows': 1
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super(MatriculaForm, self).__init__(*args, **kwargs)
        for i, (fname, field) in enumerate(self.fields.iteritems()):
            field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' form-control'

    class Meta:
        model = Matricula
        fields = [
            'servicio',
            'estudiante',
            'nivel',
            'grado',
            'institucion',
            'turno',
            'grupo',
            'observacion',
            'fechainicio',
            'fechafin',
            'tipopago',
            'descuento',
            'conceptodescuento'
        ]

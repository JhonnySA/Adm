from datetimewidget.widgets import DateWidget
from django import forms

from apps.inicio.forms_inicio.persona import PersonaForm
from ..models import Estudiante, PersonaSexos, Persona


class SearchField(forms.TextInput):
    template_name = 'campos/search.html'


class EstudianteForm(forms.ModelForm):
    personaid = forms.IntegerField(
        initial=-1,
        widget=forms.HiddenInput()
    )

    dni = forms.CharField(
        label='DNI Estudiante',
        widget=SearchField(attrs={'placeholder': 'DNI Estudiante'}),
        min_length=8,
        max_length=8
    )

    paterno = forms.CharField(
        label='Apellido Paterno',
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese apellido paterno'})
    )

    materno = forms.CharField(
        label='Apellido Materno',
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese apellido materno'})
    )

    nombre = forms.CharField(
        label='Nombre',
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese nombre'})
    )

    sexo = forms.ChoiceField(
        choices=PersonaSexos
    )

    fechanacimiento = forms.DateField(
        label='Fecha de nacimiento',
        input_formats=["%d/%m/%Y"],
        widget=DateWidget(
            attrs={"data-datepicker-type": "4", "data-provider": "datepicker-inline"},
            bootstrap_version=3,
            options={
                "format": "dd/mm/yyyy",
                # "startView": "2",
                "autoclose": "true",
                "language": "es",
                "fontAwesome": "true",
                # "todayBtn": "true",
                "clearBtn": "false"
            }
        )
    )

    observacion = forms.CharField(
        label='Alguna Observacion del Estudiante',
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Observacion'
        })
    )

    def __init__(self, *args, **kwargs):
        super(EstudianteForm, self).__init__(*args, **kwargs)

        if self.instance.pk:
            self.fields['personaid'].initial = self.instance.persona.pk
            self.fields['dni'].initial = self.instance.persona.dni
            self.fields['paterno'].initial = self.instance.persona.paterno
            self.fields['materno'].initial = self.instance.persona.materno
            self.fields['nombre'].initial = self.instance.persona.nombre
            self.fields['sexo'].initial = self.instance.persona.sexo
            self.fields['fechanacimiento'].initial = self.instance.persona.fechanacimiento

        for i, (fname, field) in enumerate(self.fields.iteritems()):
            field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' form-control'

    class Meta:
        model = Estudiante
        fields = [
            'observacion'
        ]

    def clean(self):
        estudiante = super(EstudianteForm, self).clean()
        persona = Persona.objects.filter(
            dni=estudiante['dni']
        ).exclude(
            id=estudiante['personaid']
        )
        if persona.count() > 0:
            self.add_error('dni', 'EL dni ya existe')

    def save(self, commit=True):
        estudiante = super(EstudianteForm, self).save(commit=False)
        data = self.cleaned_data

        # Preguntar x el hidden
        if data.get('personaid') == 0:
            persona = PersonaForm(data)
            persona.save()

            # Crear el estudiante
            est = Estudiante(persona=Persona.objects.get(dni=data.get('dni')), observacion=data.get('observacion'))
            est.save()
        else:
            objPersona = Persona.objects.get(pk=data.get('personaid'))
            persona = PersonaForm(data=data, instance=objPersona)
            persona.save()

            try:
                objEstudiante = Estudiante.objects.get(persona_id=data.get('personaid'))
            except Estudiante.DoesNotExist:
                objEstudiante = None

            if objEstudiante:
                objEstudiante.observacion = data.get('observacion')
                objEstudiante.save()
        return estudiante

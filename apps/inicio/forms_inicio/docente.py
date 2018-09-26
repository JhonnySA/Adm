from datetimewidget.widgets import DateWidget
from django import forms

from apps.inicio.forms_inicio.persona import PersonaForm
from apps.inicio.models import PersonaSexos, Docente, Persona


class Icheck(forms.RadioSelect):
    template_name = 'campos/icheck.html'
    input_type = 'radio'

    def get_context(self, name, value, attrs):
        context = super(Icheck, self).get_context(name, value, attrs)
        return context


class SearchField(forms.TextInput):
    template_name = 'campos/search.html'


class DocenteForm(forms.ModelForm):
    personaid = forms.IntegerField(
        initial=-1,
        widget=forms.HiddenInput()
    )

    dni = forms.CharField(
        label='DNI Docente',
        widget=SearchField(attrs={'placeholder': 'Buscar DNI'}),
        min_length=8,
        max_length=8
    )

    paterno = forms.CharField(
        label='Apellido Paterno',
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese apellido paterno'})
    )

    materno = forms.CharField(
        label='Apellido materno',
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese apellido materno'})
    )

    nombre = forms.CharField(
        label='Nombre',
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese nombre'})
    )

    sexo = forms.ChoiceField(choices=PersonaSexos)

    fechanacimiento = forms.DateField(
        label='Fecha de nacimiento',
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

    telefono = forms.CharField(
        label='Telefono',
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Telefono'
        })
    )

    celular = forms.CharField(
        label='Celular',
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Celular',
        }),
        min_length=9,
        max_length=9
    )

    correo = forms.CharField(
        label='Correo',
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Correo',
            'type': 'email'
        })
    )

    direccion = forms.CharField(
        label='Direccion',
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Direccion',
        })
    )

    profesion = forms.CharField(
        label='Profesion del docente',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Profesion del docente'})
    )

    gradoacademico = forms.CharField(
        label='Grado Academico del docente',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Grado Academico del docente'})
    )

    observacion = forms.CharField(
        label='Observacion',
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Alguna observacion',
                'cols': 30, 'rows': 1
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super(DocenteForm, self).__init__(*args, **kwargs)

        if self.instance.pk:
            self.fields['personaid'].initial = self.instance.persona.pk
            self.fields['dni'].initial = self.instance.persona.dni
            self.fields['paterno'].initial = self.instance.persona.paterno
            self.fields['materno'].initial = self.instance.persona.materno
            self.fields['nombre'].initial = self.instance.persona.nombre
            self.fields['sexo'].initial = self.instance.persona.sexo
            self.fields['fechanacimiento'].initial = self.instance.persona.fechanacimiento
            self.fields['telefono'].initial = self.instance.persona.telefono
            self.fields['celular'].initial = self.instance.persona.celular
            self.fields['correo'].initial = self.instance.persona.correo
            self.fields['direccion'].initial = self.instance.persona.direccion

        for i, (fname, field) in enumerate(self.fields.iteritems()):
            field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' form-control'

    class Meta:
        model = Docente
        fields = [
            'profesion', 'gradoacademico', 'observacion'
        ]

    def clean(self):
        docente = super(DocenteForm, self).clean()
        persona = Persona.objects.filter(
            dni=docente['dni']
        ).exclude(
            id=docente['personaid']
        )
        if persona.count() > 0:
            self.add_error('dni', 'EL dni ya existe')

    def save(self, commit=True):
        docente = super(DocenteForm, self).save(commit=False)
        data = self.cleaned_data

        # Preguntar x el hidden
        if data.get('personaid') == 0:
            persona = PersonaForm(data)
            persona.save()

            # Crear el docente
            doc = Docente(persona=Persona.objects.get(dni=data.get('dni')), profesion=data.get('profesion'),
                          gradoacademico=data.get('gradoacademico'), observacion=data.get('observacion'))
            doc.save()
        else:
            print(data.get('personaid'))
            objPersona = Persona.objects.get(pk=data.get('personaid'))
            persona = PersonaForm(data=data, instance=objPersona)
            persona.save()

            try:
                objDocente = Docente.objects.get(persona_id=data.get('personaid'))
            except Docente.DoesNotExist:
                objDocente = None

            if objDocente == None:
                # Crear el docente
                doc = Docente(persona=Persona.objects.get(dni=data.get('dni')), profesion=data.get('profesion'),
                              gradoacademico=data.get('gradoacademico'), observacion=data.get('observacion'))
                doc.save()
            else:
                objDocente.profesion = data.get('profesion')
                objDocente.gradoacademico = data.get('gradoacademico')
                objDocente.observacion = data.get('observacion')
                objDocente.save()
        return docente

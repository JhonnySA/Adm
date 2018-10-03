from django import forms

from ..models import Servicio


class ServicioForm(forms.ModelForm):
    nombre = forms.CharField(
        label='Nombre',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese el nombre'})
    )

    descripcion = forms.CharField(
        label='Descripcion',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Alguna descricion'})
    )

    unidad = forms.CharField(
        label='Unidad',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Unidad de medida'})
    )

    def __init__(self, *args, **kwargs):
        super(ServicioForm, self).__init__(*args, **kwargs)
        for i, (fname, field) in enumerate(self.fields.iteritems()):
            field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' form-control'

    class Meta:
        model = Servicio
        fields = ['nombre', 'descripcion', 'unidad']

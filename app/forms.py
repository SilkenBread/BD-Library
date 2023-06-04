from django.forms import *

from app.models import Areaconocimiento

class AreaConocimientoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['codigo_area'].widget.attrs['autofocus'] = True

    class Meta:
        model = Areaconocimiento
        fields = '__all__'
        widgets = {
            'codigo_area': TextInput(
                attrs={
                    'placeholder': 'Ingrese un codigo',
                }
            )
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
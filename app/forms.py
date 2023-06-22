from django.forms import *

from app.models import Areaconocimiento, Autor, Editorial, Libro

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
            ),
            'nombre_area': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre del área',
                }
            ),
            'desc_area': TextInput(
                attrs={
                    'placeholder': 'De una descripción del área',
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        try:
            form = super().save(commit=False)
            form.codigo_area = form.codigo_area.upper() # Convierte el campo 'codigo_area' a mayúsculas
            form.nombre_area = form.nombre_area.upper() # Convierte el campo 'nombre_area' a mayúsculas
            if self.is_valid():
                if commit:
                    form.save()
            else:
                data['error'] = self.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    
class AutorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['codigo_autor'].widget.attrs['autofocus'] = True

    class Meta:
        model = Autor
        fields = '__all__'
        widgets = {
            'primer_nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese el primer nombre',
                }
            ),
            'segundo_nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese el segundo nombre',
                }
            ),
            'primer_apellido': TextInput(
                attrs={
                    'placeholder': 'Ingrese el primer apellido',
                }
            ),
            'segundo_apellido': TextInput(
                attrs={
                    'placeholder': 'Ingrese el segundo apellido',
                }
            ),
        }
        
    def save(self, commit=True):
        data = {}
        try:
            form = super().save(commit=False)
            form.codigo_autor = form.codigo_autor.upper() # Convierte el campo 'codigo_autor' a mayúsculas
            if commit:
                form.save()
        except Exception as e:
            data['error'] = str(e)
        return data

    

class LibroForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['isbn'].widget.attrs['autofocus'] = True

    class Meta:
        model = Libro
        fields = '__all__'
        

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
    
class EditorialForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['codigo_editorial'].widget.attrs['autofocus'] = True

    class Meta:
        model = Editorial
        fields = '__all__'
        
    def save(self, commit=True):
        data = {}
        try:
            form = super().save(commit=False)
            form.codigo_editorial = form.codigo_editorial.upper() # Convierte el campo 'codigo_editorial' a mayúsculas
            form.nombre_editorial = form.nombre_editorial.upper() # Convierte el campo 'nombre_editorial' a mayúsculas
            if self.is_valid():
                if commit:
                    form.save()
            else:
                data['error'] = self.errors
        except Exception as e:
            data['error'] = str(e)
        return data

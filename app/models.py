from django.db import models
from datetime import datetime
from crum import get_current_user
from django.forms import model_to_dict
from user.models import User
from django.core.validators import RegexValidator
from django.core import serializers

class Areaconocimiento(models.Model):
    codigo_area = models.CharField(
        unique=True,
        max_length=10,
        verbose_name='Código',
        validators=[
            RegexValidator(
                regex=r'^[aA]\d{2}$',
                message=('No cumple con el estandar. Ej: A01'),
                code ='invalid_name_areaconocimiento'
            )
        ])
    nombre_area = models.CharField(max_length=20, verbose_name='Nombre')
    desc_area = models.CharField(max_length=50, null=True, blank=True, verbose_name='Descripción')
    cod_area_contenida = models.ForeignKey('self', models.DO_NOTHING, null=True, blank=True, verbose_name='Código sub área')

    def __str__(self):
        return f"{self.codigo_area} | {self.nombre_area}"
 
    class Meta:
        verbose_name_plural='Áreas de conocimiento'
        db_table = 'areaconocimiento'
    
    def toJSON(self):
        item = model_to_dict(self)
        return item


class Autor(models.Model):
    codigo_autor = models.CharField(unique=True,max_length=10, verbose_name='Código',)
    primer_nombre = models.CharField(max_length=40, verbose_name='Primer nombre')
    segundo_nombre = models.CharField(max_length=40, blank=True, null=True, verbose_name='Segundo nombre')
    primer_apellido = models.CharField(max_length=40, verbose_name='Primer apellido')
    segundo_apellido = models.CharField(max_length=40, blank=True, null=True, verbose_name='Segundo apellido')

    def __str__(self):
        return f"{self.codigo_autor} | {self.primer_nombre} {self.primer_apellido}"
    
    class Meta:
        verbose_name_plural='Autores'
        db_table = 'autor'

    def toJSON(self):
        item = model_to_dict(self)
        return item


class Editorial(models.Model):
    codigo_editorial = models.CharField(unique=True, max_length=10, verbose_name='ID'  )
    nombre_editorial = models.CharField(max_length=30, verbose_name='Nombre')
    pagina_web = models.URLField(blank=True, null=True, verbose_name='URL')
    pais_origen = models.CharField(max_length=30, blank=True, null=True, verbose_name='País origen')

    def __str__(self):
        return f"{self.codigo_editorial} | {self.nombre_editorial}"
    
    class Meta:
        verbose_name_plural='Editoriales'
        db_table = 'editorial'
        
    def toJSON(self):
        item = model_to_dict(self)
        return item


class Libro(models.Model):
    isbn = models.CharField(unique=True, max_length=30, verbose_name='ISBN')
    titulo = models.CharField(unique=True, max_length=50, verbose_name='Título')
    anio_publicacion = models.IntegerField(blank=True, null=True, verbose_name='Año publicación')
    numero_pagina = models.IntegerField(blank=True, null=True, verbose_name='Número de páginas')
    codigo_area = models.ForeignKey(Areaconocimiento, on_delete=models.PROTECT,verbose_name='Area de conocimiento')
    codigo_editorial = models.ForeignKey(Editorial, on_delete=models.PROTECT,verbose_name='Editorial')
    autores = models.ManyToManyField(Autor)

    def __str__(self):
        return f"{self.titulo} | {self.isbn}"
    
    class Meta:
        verbose_name_plural='Libros'
        db_table = 'libro'

    def toJSON(self):
        item = model_to_dict(self, exclude=['autores'])
        item['areaconocimiento']= self.codigo_area.toJSON()
        item['editorial']= self.codigo_editorial.toJSON()
        return item

class Ejemplar(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.PROTECT)
    numero_ejemplar = models.PositiveIntegerField(verbose_name='Número ejemplar')
    numero_sala = models.PositiveIntegerField(verbose_name='Número de sala')
    numero_pasillo = models.PositiveIntegerField(verbose_name='Número de pasillo')
    numero_estante = models.PositiveIntegerField(null=True, blank=True, verbose_name='Número de estante')
    numero_cajon = models.PositiveIntegerField(null=True, blank=True, verbose_name='Número de cajón')
    disponibilidad = models.BooleanField(default=True ,blank=False, null=False, verbose_name='Disponibilidad')

    def __str__(self):
        return f"{self.numero_ejemplar} | {self.libro}"
    
    class Meta:
        verbose_name_plural='Ejemplares'
        db_table = 'ejemplar'
        unique_together = (('libro', 'numero_ejemplar'))

    def toJSON(self):
        item = model_to_dict(self)
        item['datalibro'] = self.libro.toJSON()
        return item

class LibroDigital(Libro):
    formato = models.CharField(max_length=30, verbose_name='Formato')
    url = models.URLField(verbose_name='URL')
    tamanio = models.IntegerField(verbose_name='Tamaño del Libro')

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural='Libros digitales'
        db_table = 'libro_digital'

    def toJSON(self):
        item = model_to_dict(self)
        return item
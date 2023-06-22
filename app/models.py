# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime

from django.forms import model_to_dict
from user.models import User
from django.core.validators import RegexValidator

class Areaconocimiento(models.Model):
    codigo_area = models.CharField(primary_key=True, max_length=10, verbose_name='Código')
    nombre_area = models.CharField(max_length=20, verbose_name='Nombre')
    desc_area = models.CharField(max_length=50, null=True, blank=True, verbose_name='Descripción')
    cod_area_contenida = models.ForeignKey('self', models.DO_NOTHING, null=True, blank=True, verbose_name='Código sub área')

    def __str__(self):
        return self.nombre_area
 
    class Meta:
        verbose_name_plural='Áreas de conocimiento'
        db_table = 'areaconocimiento'


class Autor(models.Model):
    codigo_autor = models.CharField(primary_key=True, max_length=10, verbose_name='Código')
    primer_nombre = models.CharField(max_length=40, verbose_name='Primer nombre')
    segundo_nombre = models.CharField(max_length=40, blank=True, null=True, verbose_name='Segundo nombre')
    primer_apellido = models.CharField(max_length=40, verbose_name='Primer apellido')
    segundo_apellido = models.CharField(max_length=40, blank=True, null=True, verbose_name='Segundo apellido')

    def __str__(self):
        return self.codigo_autor
    
    class Meta:
        verbose_name_plural='Autores'
        db_table = 'autor'


class Editorial(models.Model):
    codigo_editorial = models.CharField(primary_key=True, max_length=10, verbose_name='ID'  )
    nombre_editorial = models.CharField(max_length=30, verbose_name='Nombre')
    pagina_web = models.URLField(blank=True, null=True, verbose_name='URL')
    pais_origen = models.CharField(max_length=30, blank=True, null=True, verbose_name='País origen')

    def __str__(self):
        return self.nombre_editorial
    
    class Meta:
        verbose_name_plural='Editoriales'
        db_table = 'editorial'


class Libro(models.Model):
    isbn = models.CharField(primary_key=True, max_length=30, verbose_name='ISBN')
    titulo = models.CharField(max_length=50, verbose_name='Título')
    anio_publicacion = models.IntegerField(blank=True, null=True, verbose_name='Año publicación')
    numero_pagina = models.IntegerField(blank=True, null=True, verbose_name='Número de páginas')
    codigo_area = models.ForeignKey(Areaconocimiento, on_delete=models.PROTECT,verbose_name='Area de conocimiento')
    codigo_editorial = models.ForeignKey(Editorial, on_delete=models.PROTECT,verbose_name='Editorial')
    autores = models.ManyToManyField(Autor)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name_plural='Libros'
        db_table = 'libro'

    def toJSON(self):
        item = model_to_dict(self)
        item['areaconocimiento']= self.codigo_area.nombre_area
        item['editorial']= self.codigo_editorial.nombre_editorial
        return item

class Ejemplar(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.PROTECT)
    numero_ejemplar = models.IntegerField(verbose_name='Número ejemplar')
    numero_sala = models.IntegerField(verbose_name='Número de sala')
    numero_pasillo = models.IntegerField(verbose_name='Número de pasillo')
    numero_estante = models.IntegerField(verbose_name='Número de estante')
    numero_cajon = models.IntegerField(verbose_name='Número de cajón')
    disponibilidad = models.BooleanField(default=True ,blank=False, null=False, verbose_name='Disponibilidad')

    def __str__(self):
        return self.numero_ejemplar
    
    class Meta:
        verbose_name_plural='Ejemplares'
        db_table = 'ejemplar'
        unique_together = (('libro', 'numero_ejemplar'))

    def toJSON(self):
        item = model_to_dict(self)
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
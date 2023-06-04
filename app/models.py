# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime

class Areaconocimiento(models.Model):
    codigo_area = models.CharField(primary_key=True, max_length=10, verbose_name='Código')
    nombre_area = models.CharField(max_length=20, verbose_name='Nombre')
    desc_area = models.CharField(max_length=50, verbose_name='Descripción')
    cod_area_contenida = models.ForeignKey('self', models.DO_NOTHING, db_column='cod_area_contenida', verbose_name='Código sub área')

    def __str__(self):
        return super().__str__()

    class Meta:
        verbose_name_plural='Áreas de conocimiento'
        db_table = 'areaconocimiento'


class Autor(models.Model):
    codigo_autor = models.CharField(primary_key=True, max_length=10, verbose_name='Código')
    primer_nombre = models.CharField(max_length=40, verbose_name='Primer nombre')
    segundo_nombre = models.CharField(max_length=40, blank=True, null=True, verbose_name='Segundo nombre')
    primer_apellido = models.CharField(max_length=40, verbose_name='Primer apellido')
    segundo_apellido = models.CharField(max_length=40, blank=True, null=True, verbose_name='Segundo apellido')

    class Meta:
        verbose_name_plural='Autores'
        db_table = 'autor'


class Descargalibrodigital(models.Model):
    id_usuario = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='id_usuario', primary_key=True, verbose_name='ID Usuario')
    isbn = models.ForeignKey('Librodigital', models.DO_NOTHING, db_column='isbn', verbose_name='ISBN')
    direccion_ip = models.GenericIPAddressField(blank=True, null=True, verbose_name='Dirección IP')
    fecha_descarga = models.DateTimeField(auto_now=True, verbose_name='Fecha de descarga')

    class Meta:
        
        db_table = 'descargalibrodigital'
        unique_together = (('id_usuario', 'isbn'),)


class Detalleprestamo(models.Model):
    numero_prestamo = models.OneToOneField('Prestamo', models.DO_NOTHING, db_column='numero_prestamo', primary_key=True)
    isbn = models.ForeignKey('Ejemplar', models.DO_NOTHING, db_column='isbn')
    numero_ejemplar = models.IntegerField()

    class Meta:
        
        db_table = 'detalleprestamo'
        unique_together = (('numero_prestamo', 'isbn', 'numero_ejemplar'),)


class Editorial(models.Model):
    codigo_editorial = models.CharField(primary_key=True, max_length=10, verbose_name='ID')
    nombre_editorial = models.CharField(max_length=30, verbose_name='Nombre')
    pagina_web = models.CharField(max_length=100, blank=True, null=True, verbose_name='URL')
    pais_origen = models.CharField(max_length=30, blank=True, null=True, verbose_name='País origen')

    class Meta:
        verbose_name_plural='Editoriales'
        db_table = 'editorial'


class Ejemplar(models.Model):
    isbn = models.OneToOneField('Libro', models.DO_NOTHING, db_column='isbn', primary_key=True, verbose_name='ISBN')
    numero_ejemplar = models.IntegerField()
    numero_sala = models.IntegerField()
    numero_pasillo = models.IntegerField()
    numero_estante = models.IntegerField()
    numero_cajon = models.IntegerField()
    disponibilidad = models.BooleanField(default=True ,blank=True, null=True)

    class Meta:
        verbose_name_plural='Ejemplares'
        db_table = 'ejemplar'
        unique_together = (('isbn', 'numero_ejemplar'),)


class Empleado(models.Model):
    id_empleado = models.BigIntegerField(primary_key=True)
    nombre_empleado = models.CharField(max_length=60)
    cargo_empleado = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural='Empleados'
        db_table = 'empleado'


class Estudiante(models.Model):
    id_usuario = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='id_usuario', primary_key=True)
    universidad = models.CharField(max_length=60)
    carrera = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural='Estudiantes'
        db_table = 'estudiante'


class Libro(models.Model):
    isbn = models.CharField(primary_key=True, max_length=30)
    titulo = models.CharField(max_length=50)
    anio_publicacion = models.IntegerField(blank=True, null=True)
    numero_pagina = models.IntegerField(blank=True, null=True)
    codigo_area = models.ForeignKey(Areaconocimiento, models.DO_NOTHING, db_column='codigo_area')
    codigo_editorial = models.ForeignKey(Editorial, models.DO_NOTHING, db_column='codigo_editorial')

    class Meta:
        verbose_name_plural='Libros'
        db_table = 'libro'


class Librodigital(models.Model):
    isbn = models.OneToOneField(Libro, models.DO_NOTHING, db_column='isbn', primary_key=True)
    formato = models.CharField(max_length=20, blank=True, null=True)
    url = models.CharField(max_length=200)
    tamano = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural='Libros digitales'
        db_table = 'librodigital'


class Libroescritoautor(models.Model):
    codigo_autor = models.OneToOneField(Autor, models.DO_NOTHING, db_column='codigo_autor', primary_key=True)
    isbn = models.ForeignKey(Libro, models.DO_NOTHING, db_column='isbn')

    class Meta:
        
        db_table = 'libroescritoautor'
        unique_together = (('codigo_autor', 'isbn'),)


class Multa(models.Model):
    id_usuario = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='id_usuario', primary_key=True)
    isbn = models.ForeignKey(Ejemplar, models.DO_NOTHING, db_column='isbn')
    numero_ejemplar = models.IntegerField()
    descripcion_multa = models.CharField(max_length=50, blank=True, null=True)
    valor_multa = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        verbose_name_plural='Multas'
        db_table = 'multa'
        unique_together = (('id_usuario', 'isbn', 'numero_ejemplar'),)


class Prestamo(models.Model):
    numero_prestamo = models.IntegerField(primary_key=True)
    id_usuario = models.ForeignKey(Estudiante, models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='id_empleado', blank=True, null=True)
    fecha_realizacion = models.DateField(blank=True, null=True)
    fecha_limite_entrega = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name_plural='Prestamos'
        db_table = 'prestamo'


class Profesor(models.Model):
    id_usuario = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='id_usuario', primary_key=True)
    titulo = models.CharField(max_length=30)
    dependencia = models.CharField(max_length=30, blank=True, null=True)
    area_interes = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        verbose_name_plural='Profesores'
        db_table = 'profesor'


class Solicitudlibronuevo(models.Model):
    num_consecutivo = models.IntegerField(primary_key=True)
    descripcion_solicitud = models.CharField(max_length=100)
    isbn = models.CharField(max_length=30)
    titulo_libro = models.CharField(max_length=60)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='id_empleado')
    fecha_realizacion = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name_plural='Solicitudes de nuevos libros'
        db_table = 'solicitudlibronuevo'


class Usuario(models.Model):
    id_usuario = models.BigIntegerField(primary_key=True, verbose_name='ID')
    nombre_usuario = models.CharField(max_length=60, verbose_name='Nombre')
    email_usuario = models.CharField(max_length=60, verbose_name='Correo')
    telefono_usuario = models.BigIntegerField(blank=True, null=True, verbose_name='Teléfono')

    class Meta:
        verbose_name_plural='Usuarios'
        db_table = 'usuario'

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Areaconocimiento(models.Model):
    cod_area = models.CharField(primary_key=True, max_length=10)
    desc_area = models.CharField(max_length=100, blank=True, null=True)
    nombre_area = models.CharField(max_length=30, blank=True, null=True)
    cod_area_contenida = models.ForeignKey('self', models.DO_NOTHING, db_column='cod_area_contenida', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'areaconocimiento'


class Autor(models.Model):
    cod_autor = models.CharField(primary_key=True, max_length=20)
    segundo_apellido = models.CharField(max_length=20, blank=True, null=True)
    primer_apellido = models.CharField(max_length=20, blank=True, null=True)
    segundo_nombre = models.CharField(max_length=20, blank=True, null=True)
    primer_nombre = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'autor'


class Descarga(models.Model):
    id_usuario = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='id_usuario', primary_key=True)  # The composite primary key (id_usuario, isbn) found, that is not supported. The first column is selected.
    isbn = models.ForeignKey('Digital', models.DO_NOTHING, db_column='isbn')

    class Meta:
        managed = False
        db_table = 'descarga'
        unique_together = (('id_usuario', 'isbn'),)


class Digital(models.Model):
    isbn = models.OneToOneField('Libro', models.DO_NOTHING, db_column='isbn', primary_key=True)
    formato = models.CharField(max_length=10, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    tamano = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'digital'


class Editorial(models.Model):
    codigo_editorial = models.CharField(primary_key=True, max_length=30)
    nombre_editorial = models.CharField(max_length=30, blank=True, null=True)
    pagina_web = models.CharField(max_length=200, blank=True, null=True)
    pais_origen = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'editorial'


class Ejemplar(models.Model):
    isbn = models.OneToOneField('Libro', models.DO_NOTHING, db_column='isbn', primary_key=True)  # The composite primary key (isbn, num_ejemplar) found, that is not supported. The first column is selected.
    num_ejemplar = models.IntegerField()
    nom_sala = models.IntegerField(blank=True, null=True)
    num_pasillo = models.IntegerField(blank=True, null=True)
    num_estante = models.IntegerField(blank=True, null=True)
    num_cajon = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ejemplar'
        unique_together = (('isbn', 'num_ejemplar'),)


class Empleado(models.Model):
    id_empleado = models.CharField(primary_key=True, max_length=20)
    nombre_empl = models.CharField(max_length=60, blank=True, null=True)
    cargo_empl = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado'


class Escrito(models.Model):
    cod_autor = models.OneToOneField(Autor, models.DO_NOTHING, db_column='cod_autor', primary_key=True)  # The composite primary key (cod_autor, isbn) found, that is not supported. The first column is selected.
    isbn = models.ForeignKey('Libro', models.DO_NOTHING, db_column='isbn')

    class Meta:
        managed = False
        db_table = 'escrito'
        unique_together = (('cod_autor', 'isbn'),)


class Estudiante(models.Model):
    id_usuario = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='id_usuario', primary_key=True)
    universidad = models.CharField(max_length=60, blank=True, null=True)
    carrera = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estudiante'


class Libro(models.Model):
    isbn = models.CharField(primary_key=True, max_length=30)
    titulo = models.CharField(max_length=60, blank=True, null=True)
    ano_publicacion = models.CharField(max_length=4, blank=True, null=True)
    numero_pagina = models.IntegerField(blank=True, null=True)
    cod_area = models.ForeignKey(Areaconocimiento, models.DO_NOTHING, db_column='cod_area', blank=True, null=True)
    codigo_editorial = models.ForeignKey(Editorial, models.DO_NOTHING, db_column='codigo_editorial', blank=True, null=True)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        managed = False
        db_table = 'libro'
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['isbn']


class Multa(models.Model):
    id_usuario = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='id_usuario', primary_key=True)  # The composite primary key (id_usuario, isbn, num_ejemplar) found, that is not supported. The first column is selected.
    isbn = models.OneToOneField(Ejemplar, models.DO_NOTHING, db_column='isbn')
    num_ejemplar = models.IntegerField()
    desc_multa = models.IntegerField(blank=True, null=True)
    valor_multa = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'multa'
        unique_together = (('id_usuario', 'isbn', 'num_ejemplar'),)


class Prestamo(models.Model):
    num_prestamo = models.IntegerField(primary_key=True)
    fecha_realizacion = models.CharField(max_length=20, blank=True, null=True)
    fecha_limite_devolucion = models.CharField(max_length=20, blank=True, null=True)
    fecha_entrega_devolucion = models.CharField(max_length=20, blank=True, null=True)
    id_usuario = models.ForeignKey(Estudiante, models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='id_empleado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prestamo'


class Profesor(models.Model):
    id_usuario = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='id_usuario', primary_key=True)
    titulo = models.CharField(max_length=30, blank=True, null=True)
    dependencia = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profesor'


class Profesorareadeinteres(models.Model):
    id_usuario = models.OneToOneField(Profesor, models.DO_NOTHING, db_column='id_usuario', primary_key=True)  # The composite primary key (id_usuario, area_interes) found, that is not supported. The first column is selected.
    area_interes = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'profesorareadeinteres'
        unique_together = (('id_usuario', 'area_interes'),)


class Solicitudlibronuevo(models.Model):
    num_consecutivo = models.IntegerField(primary_key=True)
    descripcion_solicitud = models.CharField(max_length=200, blank=True, null=True)
    isbn = models.CharField(max_length=30, blank=True, null=True)
    fecha = models.CharField(max_length=20, blank=True, null=True)
    titulo_libro = models.CharField(max_length=60, blank=True, null=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='id_empleado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solicitudlibronuevo'


class Tiene(models.Model):
    num_prestamo = models.OneToOneField(Prestamo, models.DO_NOTHING, db_column='num_prestamo', primary_key=True)  # The composite primary key (num_prestamo, isbn, num_ejemplar) found, that is not supported. The first column is selected.
    isbn = models.OneToOneField(Ejemplar, models.DO_NOTHING, db_column='isbn')
    num_ejemplar = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tiene'
        unique_together = (('num_prestamo', 'isbn', 'num_ejemplar'),)


class Usuario(models.Model):
    id_usuario = models.CharField(primary_key=True, max_length=20)
    nombre_usuario = models.CharField(max_length=60, blank=True, null=True)
    email_usuario = models.CharField(max_length=60, blank=True, null=True)
    telefono_usuario = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'

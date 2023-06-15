# Generated by Django 4.2 on 2023-06-15 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_areaconocimiento_cod_area_contenida'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='detalleprestamo',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='detalleprestamo',
            name='isbn',
        ),
        migrations.RemoveField(
            model_name='detalleprestamo',
            name='numero_prestamo',
        ),
        migrations.AlterUniqueTogether(
            name='ejemplar',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='ejemplar',
            name='isbn',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='id_usuario',
        ),
        migrations.RemoveField(
            model_name='librodigital',
            name='isbn',
        ),
        migrations.AlterUniqueTogether(
            name='libroescritoautor',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='libroescritoautor',
            name='codigo_autor',
        ),
        migrations.RemoveField(
            model_name='libroescritoautor',
            name='isbn',
        ),
        migrations.AlterUniqueTogether(
            name='multa',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='multa',
            name='id_usuario',
        ),
        migrations.RemoveField(
            model_name='multa',
            name='isbn',
        ),
        migrations.RemoveField(
            model_name='prestamo',
            name='id_empleado',
        ),
        migrations.RemoveField(
            model_name='prestamo',
            name='id_usuario',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='id_usuario',
        ),
        migrations.RemoveField(
            model_name='solicitudlibronuevo',
            name='id_empleado',
        ),
        migrations.RemoveField(
            model_name='solicitudlibronuevo',
            name='id_usuario',
        ),
        migrations.AlterField(
            model_name='areaconocimiento',
            name='cod_area_contenida',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.areaconocimiento', verbose_name='Código sub área'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='anio_publicacion',
            field=models.IntegerField(blank=True, null=True, verbose_name='Año publicación'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='codigo_area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.areaconocimiento', verbose_name='Código de área'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='codigo_editorial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.editorial', verbose_name='Código de editorial'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='isbn',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='numero_pagina',
            field=models.IntegerField(blank=True, null=True, verbose_name='Número de páginas'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='titulo',
            field=models.CharField(max_length=50, verbose_name='Título'),
        ),
        migrations.DeleteModel(
            name='Descargalibrodigital',
        ),
        migrations.DeleteModel(
            name='Detalleprestamo',
        ),
        migrations.DeleteModel(
            name='Ejemplar',
        ),
        migrations.DeleteModel(
            name='Empleado',
        ),
        migrations.DeleteModel(
            name='Estudiante',
        ),
        migrations.DeleteModel(
            name='Librodigital',
        ),
        migrations.DeleteModel(
            name='Libroescritoautor',
        ),
        migrations.DeleteModel(
            name='Multa',
        ),
        migrations.DeleteModel(
            name='Prestamo',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
        migrations.DeleteModel(
            name='Solicitudlibronuevo',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
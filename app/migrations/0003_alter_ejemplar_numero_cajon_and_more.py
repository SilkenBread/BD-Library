# Generated by Django 4.2 on 2023-06-25 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_libro_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ejemplar',
            name='numero_cajon',
            field=models.PositiveIntegerField(verbose_name='Número de cajón'),
        ),
        migrations.AlterField(
            model_name='ejemplar',
            name='numero_ejemplar',
            field=models.PositiveIntegerField(verbose_name='Número ejemplar'),
        ),
        migrations.AlterField(
            model_name='ejemplar',
            name='numero_estante',
            field=models.PositiveIntegerField(verbose_name='Número de estante'),
        ),
        migrations.AlterField(
            model_name='ejemplar',
            name='numero_pasillo',
            field=models.PositiveIntegerField(verbose_name='Número de pasillo'),
        ),
        migrations.AlterField(
            model_name='ejemplar',
            name='numero_sala',
            field=models.PositiveIntegerField(verbose_name='Número de sala'),
        ),
    ]

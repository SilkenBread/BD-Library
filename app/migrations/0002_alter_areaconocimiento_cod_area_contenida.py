# Generated by Django 4.2 on 2023-06-04 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areaconocimiento',
            name='cod_area_contenida',
            field=models.ForeignKey(blank=True, db_column='cod_area_contenida', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.areaconocimiento', verbose_name='Código sub área'),
        ),
    ]
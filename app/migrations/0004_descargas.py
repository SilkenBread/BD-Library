# Generated by Django 4.2 on 2023-06-26 03:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_librodigital_libro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Descargas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_descarga', models.DateTimeField(default=django.utils.timezone.now)),
                ('direccion_ip', models.GenericIPAddressField(verbose_name='Dirección IP')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
    ]

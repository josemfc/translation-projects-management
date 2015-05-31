# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proyectos', '0002_tarea_archivo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='archivo',
        ),
        migrations.AddField(
            model_name='proyecto',
            name='creador',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarea',
            name='asignada_a',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_pub',
            field=models.DateTimeField(null=True, verbose_name='Fecha de publicacion', blank=True),
        ),
    ]

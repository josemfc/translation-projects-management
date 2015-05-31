# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0003_auto_20150414_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='terminado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tarea',
            name='num_horas',
            field=models.IntegerField(verbose_name='Num. de horas estimado', default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarea',
            name='terminada',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tarea',
            name='tipo_tarea',
            field=models.CharField(default='T', max_length=15, choices=[('T', 'Traducción'), ('R', 'Revisión')]),
        ),
    ]

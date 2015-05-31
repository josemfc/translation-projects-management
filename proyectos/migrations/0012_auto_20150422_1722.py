# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0011_remove_tarea_terminada'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='terminado',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tarea',
            name='terminada',
            field=models.BooleanField(default=False),
        ),
    ]

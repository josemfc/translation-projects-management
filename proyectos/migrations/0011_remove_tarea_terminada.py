# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0010_remove_proyecto_terminado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='terminada',
        ),
    ]

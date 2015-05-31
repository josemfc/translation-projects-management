# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0014_tarea_no_necesario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea',
            name='no_necesario',
        ),
    ]

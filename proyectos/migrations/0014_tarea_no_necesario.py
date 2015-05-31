# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0013_auto_20150422_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='no_necesario',
            field=models.CharField(null=True, blank=True, max_length=1),
        ),
    ]

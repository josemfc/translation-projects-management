# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import proyectos.models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0007_auto_20150422_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='original',
            field=models.FileField(verbose_name='Texto original', upload_to=proyectos.models.upload_path_handler, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='traducido',
            field=models.FileField(verbose_name='Texto traducido', upload_to=proyectos.models.upload_path_handler, blank=True, null=True),
        ),
    ]

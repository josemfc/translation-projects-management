# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import proyectos.models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0006_auto_20150422_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='original',
            field=models.FileField(verbose_name='Texto original', default=0, upload_to=proyectos.models.upload_path_handler),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarea',
            name='traducido',
            field=models.FileField(verbose_name='Texto traducido', default=0, upload_to=proyectos.models.upload_path_handler),
            preserve_default=False,
        ),
    ]

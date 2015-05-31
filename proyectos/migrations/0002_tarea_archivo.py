# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='archivo',
            field=models.FileField(null=True, upload_to='media/', blank=True),
            preserve_default=True,
        ),
    ]

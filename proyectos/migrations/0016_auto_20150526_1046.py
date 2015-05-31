# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0015_remove_tarea_no_necesario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_pub',
            field=models.DateTimeField(verbose_name='Fecha de publicacion', default=datetime.datetime(2015, 5, 26, 8, 46, 6, 248853, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

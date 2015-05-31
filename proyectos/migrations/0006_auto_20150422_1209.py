# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0005_auto_20150422_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='terminado',
            field=models.BooleanField(default=0),
        ),
    ]

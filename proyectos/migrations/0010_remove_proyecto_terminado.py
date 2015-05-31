# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0009_auto_20150422_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyecto',
            name='terminado',
        ),
    ]

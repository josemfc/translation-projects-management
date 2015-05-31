# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0008_auto_20150422_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='terminado',
            field=models.NullBooleanField(default=False),
        ),
    ]

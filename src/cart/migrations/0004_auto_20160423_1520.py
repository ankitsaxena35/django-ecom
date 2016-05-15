# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20160423_1449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='item',
            new_name='items',
        ),
    ]

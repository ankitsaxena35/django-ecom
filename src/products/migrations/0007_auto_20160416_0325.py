# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_productfeatured_test_css'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productfeatured',
            name='test_css',
            field=models.CharField(max_length=6),
        ),
    ]

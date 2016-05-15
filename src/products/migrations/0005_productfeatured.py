# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20160409_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductFeatured',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120, blank=True)),
                ('image', models.ImageField(upload_to=b'featured/')),
                ('background_image', models.BooleanField(default=False)),
                ('text', models.CharField(max_length=120, null=True, blank=True)),
                ('text_right', models.BooleanField(default=False)),
                ('show_price', models.BooleanField(default=True)),
                ('active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(to='products.Products')),
            ],
        ),
    ]

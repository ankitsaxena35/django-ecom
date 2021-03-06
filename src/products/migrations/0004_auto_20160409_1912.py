# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100)),
                ('description', models.TextField(null=True, blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.ManyToManyField(to='products.Category'),
        ),
        migrations.AddField(
            model_name='products',
            name='default',
            field=models.ForeignKey(related_name='dafault_category', blank=True, to='products.Category', null=True),
        ),
    ]

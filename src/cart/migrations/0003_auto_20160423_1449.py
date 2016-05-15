# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20160416_0325'),
        ('cart', '0002_remove_cart_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='item',
            field=models.ManyToManyField(to='products.Variations', through='cart.CartItem'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(default=1, to='cart.Cart'),
            preserve_default=False,
        ),
    ]

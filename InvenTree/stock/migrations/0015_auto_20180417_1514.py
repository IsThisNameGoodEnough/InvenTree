# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 15:14
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0014_auto_20180418_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockitem',
            name='status',
            field=models.PositiveIntegerField(choices=[(10, 'OK'), (60, 'Destroyed'), (50, 'Attention needed'), (55, 'Damaged')], default=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-25 09:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0003_auto_20160324_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='label',
            name='LABEL_WIKI_EN',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

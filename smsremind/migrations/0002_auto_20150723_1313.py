# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smsremind', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='job',
            name='receiver',
        ),
        migrations.AddField(
            model_name='tracker',
            name='contact',
            field=models.CharField(default=256714128718, max_length=14),
            preserve_default=False,
        ),
    ]

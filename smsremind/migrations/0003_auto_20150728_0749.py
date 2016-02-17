# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smsremind', '0002_auto_20150723_1313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tracker',
            old_name='reminder',
            new_name='is_set',
        ),
        migrations.AddField(
            model_name='tracker',
            name='is_active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]

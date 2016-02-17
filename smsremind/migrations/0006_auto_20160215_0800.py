# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smsremind', '0005_auto_20160211_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='dname',
            field=models.CharField(default=b'', max_length=25, choices=[(0, b''), (1, b'Robert'), (2, b'Denis'), (3, b'Steve'), (4, b'Andrew'), (5, b'Floriante'), (6, b'Kennedy'), (7, b'Sylvia'), (8, b'Josh'), (9, b'Micheal'), (10, b'Kitamirike'), (11, b'Joy'), (12, b'Patrick')]),
        ),
        migrations.AlterField(
            model_name='contract',
            name='expiry',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='contract',
            name='signed',
            field=models.DateField(),
        ),
    ]

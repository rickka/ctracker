# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smsremind', '0006_auto_20160215_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='dname',
            field=models.CharField(default=b'', max_length=25, choices=[(b'', b''), (b'Robert', b'Robert'), (b'Denis', b'Denis'), (b'Steve', b'Steve'), (b'Andrew', b'Andrew'), (b'Floriante', b'Floriante'), (b'Kennedy', b'Kennedy'), (b'Sylvia', b'Sylvia'), (b'Josh', b'Josh'), (b'Micheal', b'Micheal'), (b'Kitamirike', b'Kitamirike'), (b'Joy', b'Joy'), (b'Patrick', b'Patrick')]),
        ),
    ]

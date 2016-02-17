# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smsremind', '0004_auto_20160211_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='dname',
            field=models.CharField(default=b'', max_length=25, choices=[(b'', b''), (b'robert', b'Robert'), (b'denis', b'Denis'), (b'steve', b'Steve'), (b'andrew', b'Andrew'), (b'floriante', b'Floriante'), (b'kennedy', b'Kennedy'), (b'sylvia', b'Sylvia'), (b'josh', b'Josh'), (b'micheal', b'Micheal'), (b'kitamirike', b'Kitamirike'), (b'joy', b'Joy'), (b'patrick', b'Patrick')]),
        ),
    ]

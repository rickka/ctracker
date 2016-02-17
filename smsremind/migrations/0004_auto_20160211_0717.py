# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smsremind', '0003_auto_20150728_0749'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('signed', models.DateTimeField()),
                ('expiry', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('clname', models.CharField(max_length=50)),
                ('clcontact', models.CharField(max_length=14)),
                ('altcontact', models.CharField(max_length=14, blank=True)),
                ('dname', models.CharField(max_length=25)),
                ('dcontact', models.CharField(max_length=14)),
                ('demail', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_set', models.BooleanField(default=False)),
                ('count', models.IntegerField(default=0)),
                ('contract', models.ForeignKey(to='smsremind.Contract')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='tracker',
            name='job',
        ),
        migrations.DeleteModel(
            name='Job',
        ),
        migrations.RemoveField(
            model_name='tracker',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Tracker',
        ),
        migrations.RenameField(
            model_name='smslog',
            old_name='message',
            new_name='text',
        ),
        migrations.AddField(
            model_name='owner',
            name='email',
            field=models.EmailField(default=b'mail.dmarkmobile.com', max_length=30),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='smslog',
            name='tstamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='owner',
            name='name',
            field=models.CharField(max_length=25),
        ),
    ]

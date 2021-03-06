# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=500)),
                ('start', models.DateTimeField()),
                ('deadline', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

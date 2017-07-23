# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListUser',
            fields=[
                ('email', models.EmailField(serialize=False, max_length=254, primary_key=True)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('email', models.EmailField(max_length=254)),
                ('uid', models.CharField(max_length=36, default=uuid.uuid4)),
            ],
        ),
    ]

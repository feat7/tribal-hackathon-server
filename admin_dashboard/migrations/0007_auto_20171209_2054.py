# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0006_auto_20171209_2032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='population',
            name='place',
        ),
        migrations.AddField(
            model_name='place',
            name='population',
            field=models.ForeignKey(default=0, to='admin_dashboard.Population'),
        ),
    ]

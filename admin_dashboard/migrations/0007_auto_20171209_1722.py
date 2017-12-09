# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0006_auto_20171209_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allocation',
            name='place_id',
            field=models.ForeignKey(null=True, to='admin_dashboard.Place', blank=True),
        ),
        migrations.AlterField(
            model_name='allocation',
            name='population_id',
            field=models.ForeignKey(null=True, to='admin_dashboard.Population', blank=True),
        ),
        migrations.AlterField(
            model_name='allocation',
            name='scheme_id',
            field=models.ForeignKey(null=True, to='admin_dashboard.Scheme', blank=True),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='allocation_id',
            field=models.ForeignKey(null=True, to='admin_dashboard.Allocation', blank=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='upper_node',
            field=models.ForeignKey(null=True, default=0, to='admin_dashboard.Place', blank=True),
        ),
        migrations.AlterField(
            model_name='population',
            name='place_id',
            field=models.ForeignKey(null=True, to='admin_dashboard.Place', blank=True),
        ),
    ]

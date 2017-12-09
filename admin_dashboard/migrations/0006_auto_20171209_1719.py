# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0005_announcement_complaint'),
    ]

    operations = [
        migrations.AddField(
            model_name='population',
            name='place_id',
            field=models.ForeignKey(default=0, to='admin_dashboard.Place', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='allocation',
            name='place_id',
            field=models.ForeignKey(blank=True, to='admin_dashboard.Place'),
        ),
        migrations.AlterField(
            model_name='allocation',
            name='population_id',
            field=models.ForeignKey(blank=True, to='admin_dashboard.Population'),
        ),
        migrations.AlterField(
            model_name='allocation',
            name='scheme_id',
            field=models.ForeignKey(blank=True, to='admin_dashboard.Scheme'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='allocation_id',
            field=models.ForeignKey(blank=True, to='admin_dashboard.Allocation'),
        ),
        migrations.AlterField(
            model_name='place',
            name='upper_node',
            field=models.ForeignKey(default=0, to='admin_dashboard.Place', blank=True),
        ),
    ]

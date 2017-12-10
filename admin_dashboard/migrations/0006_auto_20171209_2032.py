# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0005_announcement_complaint'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allocation',
            old_name='place_id',
            new_name='place',
        ),
        migrations.RenameField(
            model_name='allocation',
            old_name='scheme_id',
            new_name='scheme',
        ),
        migrations.RenameField(
            model_name='complaint',
            old_name='allocation_id',
            new_name='allocation',
        ),
        migrations.RemoveField(
            model_name='allocation',
            name='population_id',
        ),
        migrations.AddField(
            model_name='population',
            name='place',
            field=models.ForeignKey(to='admin_dashboard.Place', default=0),
        ),
        migrations.AlterField(
            model_name='place',
            name='upper_node',
            field=models.ForeignKey(blank=True, to='admin_dashboard.Place', default=0, null=True),
        ),
    ]

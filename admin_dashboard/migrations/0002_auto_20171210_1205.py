# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0001_initial'),
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
        migrations.RemoveField(
            model_name='allocation',
            name='population_id',
        ),
        migrations.AlterField(
            model_name='allocation',
            name='id',
            field=models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False),
        ),
    ]

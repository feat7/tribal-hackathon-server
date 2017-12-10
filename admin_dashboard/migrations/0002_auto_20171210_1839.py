# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='allocation_id',
            new_name='allocation',
        ),
        migrations.AddField(
            model_name='place',
            name='population',
            field=models.ForeignKey(blank=True, null=True, to='admin_dashboard.Population'),
        ),
        migrations.AddField(
            model_name='scheme',
            name='dis_likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='scheme',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='place',
            name='id',
            field=models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False),
        ),
    ]

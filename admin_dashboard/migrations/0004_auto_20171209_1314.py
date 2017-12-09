# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0003_population'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allocation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('description', models.TextField()),
                ('allocated_amount', models.BigIntegerField()),
                ('used_amount', models.BigIntegerField()),
                ('status', models.CharField(default='NO', max_length=20, choices=[('YES', 'YES'), ('NO', 'NO')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('place_id', models.ForeignKey(to='admin_dashboard.Place')),
            ],
        ),
        migrations.RenameField(
            model_name='population',
            old_name='percent_tribal_population',
            new_name='tribal_population_percent',
        ),
        migrations.RemoveField(
            model_name='population',
            name='name',
        ),
        migrations.AddField(
            model_name='allocation',
            name='population_id',
            field=models.ForeignKey(to='admin_dashboard.Population'),
        ),
        migrations.AddField(
            model_name='allocation',
            name='scheme_id',
            field=models.ForeignKey(to='admin_dashboard.Scheme'),
        ),
    ]

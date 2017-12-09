# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0002_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('total_population', models.BigIntegerField()),
                ('tribal_population', models.BigIntegerField()),
                ('percent_tribal_population', models.IntegerField()),
                ('status', models.CharField(max_length=20, choices=[('YES', 'YES'), ('NO', 'NO')], default='NO')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

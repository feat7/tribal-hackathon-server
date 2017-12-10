# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0007_auto_20171209_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=20, default='NO')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='allocation',
            name='place',
            field=models.ForeignKey(to='admin_dashboard.Place', related_name='place_details'),
        ),
        migrations.AddField(
            model_name='scheme',
            name='department',
            field=models.ForeignKey(default=0, to='admin_dashboard.Department'),
        ),
    ]

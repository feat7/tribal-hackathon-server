# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allocation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('description', models.TextField()),
                ('allocated_amount', models.BigIntegerField()),
                ('used_amount', models.BigIntegerField()),
                ('status', models.CharField(max_length=20, default='NO', choices=[('YES', 'YES'), ('NO', 'NO')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('status', models.CharField(max_length=20, default='NO', choices=[('YES', 'YES'), ('NO', 'NO')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('status', models.CharField(max_length=20, default='NO', choices=[('YES', 'YES'), ('NO', 'NO')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('allocation_id', models.ForeignKey(to='admin_dashboard.Allocation')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('status', models.CharField(max_length=20, default='NO', choices=[('YES', 'YES'), ('NO', 'NO')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('type', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20, default='NO', choices=[('YES', 'YES'), ('NO', 'NO')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('upper_node', models.ForeignKey(blank=True, to='admin_dashboard.Place', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('total_population', models.BigIntegerField()),
                ('tribal_population', models.BigIntegerField()),
                ('tribal_population_percent', models.IntegerField()),
                ('status', models.CharField(max_length=20, default='NO', choices=[('YES', 'YES'), ('NO', 'NO')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('used_amount', models.FloatField()),
                ('allocated_amount', models.FloatField()),
                ('status', models.CharField(max_length=20, default='NO', choices=[('YES', 'YES'), ('NO', 'NO')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(default=0, to='admin_dashboard.Department', related_name='Scheme')),
            ],
        ),
        migrations.AddField(
            model_name='allocation',
            name='place_id',
            field=models.ForeignKey(to='admin_dashboard.Place'),
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

# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-10 12:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('allocated_amount', models.BigIntegerField()),
                ('used_amount', models.BigIntegerField()),
                ('status', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('allocation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.Allocation')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('type', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('upper_node', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.Place')),
            ],
        ),
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total_population', models.BigIntegerField()),
                ('tribal_population', models.BigIntegerField()),
                ('tribal_population_percent', models.IntegerField()),
                ('status', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('used_amount', models.FloatField()),
                ('allocated_amount', models.FloatField()),
                ('status', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Scheme', to='admin_dashboard.Department')),
            ],
        ),
        migrations.AddField(
            model_name='allocation',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.Place'),
        ),
        migrations.AddField(
            model_name='allocation',
            name='scheme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_dashboard.Scheme'),
        ),
    ]

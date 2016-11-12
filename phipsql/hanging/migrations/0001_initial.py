# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 13:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Responds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('situation', models.CharField(max_length=100)),
                ('saying', models.TextField()),
                ('ratio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Right',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter', models.CharField(max_length=1)),
                ('state', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Terminal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=42)),
                ('rgt', models.IntegerField()),
                ('wrg', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Wrong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter', models.CharField(max_length=1)),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hanging.Word')),
            ],
        ),
        migrations.AddField(
            model_name='right',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hanging.Word'),
        ),
    ]
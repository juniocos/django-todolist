# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-18 18:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('list', '0006_delete_lista'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=1000)),
                ('ordem', models.IntegerField()),
            ],
        ),
    ]
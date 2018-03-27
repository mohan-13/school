# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-27 12:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='parents',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='children_of', to='academics.Parent'),
        ),
    ]

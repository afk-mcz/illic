# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 18:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0008_therapy_large_image'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cms.Therapist'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entry',
            name='slug',
            field=models.SlugField(editable=False, max_length=140, unique=True),
        ),
    ]
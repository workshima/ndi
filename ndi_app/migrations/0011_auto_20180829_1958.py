# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-29 16:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ndi_app', '0010_auto_20180829_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='downloadfiles',
            name='expertise',
        ),
        migrations.RemoveField(
            model_name='servicesofexpertise',
            name='expertise',
        ),
        migrations.AddField(
            model_name='downloadfiles',
            name='activity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='download_file', to='ndi_app.Activity', verbose_name='Файл для экспертизы'),
        ),
        migrations.AddField(
            model_name='servicesofexpertise',
            name='activity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_of_activity', to='ndi_app.Activity', verbose_name='Услуга для экспертизы'),
        ),
        migrations.DeleteModel(
            name='Expertise',
        ),
    ]

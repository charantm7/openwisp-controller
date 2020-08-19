# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-11 18:35
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0005_populate_device'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='device',
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to='config.Device'
            ),
        ),
    ]

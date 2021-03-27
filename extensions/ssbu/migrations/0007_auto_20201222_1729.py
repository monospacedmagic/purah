# Generated by Django 3.1.4 on 2020-12-22 17:29

from django.db import migrations
import extensions.ssbu.dsr


class Migration(migrations.Migration):

    dependencies = [
        ('ssbu', '0006_auto_20201222_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ruleset',
            name='dsr_variation',
        ),
        migrations.AddField(
            model_name='ruleset',
            name='dsr',
            field=extensions.ssbu.dsr.DSRField(default=extensions.ssbu.dsr.DSR['on'], max_length=32),
        ),
    ]

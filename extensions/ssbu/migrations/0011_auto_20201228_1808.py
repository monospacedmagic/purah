# Generated by Django 3.1.4 on 2020-12-28 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ssbu', '0010_auto_20201228_1651'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='match',
            options={'get_latest_by': 'id'},
        ),
    ]

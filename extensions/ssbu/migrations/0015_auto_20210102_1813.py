# Generated by Django 3.1.4 on 2021-01-02 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ssbu', '0014_auto_20210102_1338'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='match',
            options={'get_latest_by': 'started_at'},
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-09 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sents', '0010_table_fuller_table_sanctioner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='fuller',
        ),
    ]

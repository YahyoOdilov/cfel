# Generated by Django 4.0.4 on 2022-05-05 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_table_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table',
            old_name='user_id',
            new_name='user',
        ),
    ]

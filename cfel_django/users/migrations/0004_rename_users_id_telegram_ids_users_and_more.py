# Generated by Django 4.0.4 on 2022-04-21 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_telegram_ids_users_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='telegram_ids',
            old_name='users_id',
            new_name='users',
        ),
        migrations.RenameField(
            model_name='user_domains',
            old_name='users_id',
            new_name='users',
        ),
    ]
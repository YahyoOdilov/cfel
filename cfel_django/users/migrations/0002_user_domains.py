# Generated by Django 4.0.4 on 2022-04-20 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_domains',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_domain', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(null=True)),
                ('users_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.table')),
            ],
        ),
    ]

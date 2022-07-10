# Generated by Django 4.0.2 on 2022-03-15 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('creator_id', models.BigIntegerField()),
                ('linked_id', models.BigIntegerField()),
                ('initial', models.BigIntegerField(null=True)),
                ('date', models.CharField(max_length=255)),
                ('sanction', models.BooleanField(null=True)),
                ('sanction_date', models.CharField(max_length=255, null=True)),
                ('overall', models.BigIntegerField(null=True)),
            ],
        ),
    ]

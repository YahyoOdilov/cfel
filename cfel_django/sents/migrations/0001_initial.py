

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add_values',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('value', models.BigIntegerField()),
                ('reason_add', models.CharField(max_length=255)),
                ('production_id', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Bag_value',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('product_id', models.BigIntegerField()),
                ('product_value', models.BigIntegerField()),
                ('loading_paid', models.BigIntegerField(null=True)),
                ('production_id', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Loading',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=255)),
                ('fuller_in_id', models.BigIntegerField()),
                ('sents_id', models.BigIntegerField(null=True)),
                ('overall', models.BigIntegerField(null=True)),
                ('sanction', models.BooleanField(null=True)),
                ('sanction_date', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('product_id', models.BigIntegerField()),
                ('product_value', models.BigIntegerField()),
                ('product_price', models.BigIntegerField(null=True)),
                ('production_id', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=255)),
                ('production_id', models.BigIntegerField(null=True)),
                ('producter_id', models.BigIntegerField(null=True)),
                ('provider_id', models.BigIntegerField(null=True)),
                ('sanction', models.BooleanField(null=True)),
                ('sanction_date', models.CharField(max_length=255, null=True)),
                ('producter_comment', models.CharField(max_length=255, null=True)),
                ('provider_comment', models.CharField(max_length=255, null=True)),
                ('overall', models.BigIntegerField(null=True)),
            ],
        ),
    ]

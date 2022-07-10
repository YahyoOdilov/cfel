# Generated by Django 4.0.4 on 2022-05-05 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_users_id_telegram_ids_users_and_more'),
        ('product', '0002_alter_table_user_id'),
        ('sents', '0002_alter_loading_sanction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.table'),
        ),
        migrations.AlterField(
            model_name='table',
            name='producter_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='producter+', to='users.table'),
        ),
        migrations.AlterField(
            model_name='table',
            name='provider_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='provider+', to='users.table'),
        ),
        migrations.CreateModel(
            name='Product_back',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('product_id', models.BigIntegerField()),
                ('product_value', models.BigIntegerField()),
                ('product_price', models.BigIntegerField(null=True)),
                ('users_domain_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sents.table')),
            ],
        ),
    ]
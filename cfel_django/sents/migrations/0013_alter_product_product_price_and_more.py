# Generated by Django 4.0.4 on 2022-06-02 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sents', '0012_alter_product_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_value',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='storage',
            name='initial',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='table',
            name='overall',
            field=models.FloatField(null=True),
        ),
    ]

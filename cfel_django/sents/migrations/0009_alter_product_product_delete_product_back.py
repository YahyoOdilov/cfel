# Generated by Django 4.0.4 on 2022-05-08 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sents', '0008_storage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='storage+', to='sents.storage'),
        ),
        migrations.DeleteModel(
            name='Product_back',
        ),
    ]

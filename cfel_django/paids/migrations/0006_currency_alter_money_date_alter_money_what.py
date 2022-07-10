# Generated by Django 4.0.4 on 2022-05-06 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paids', '0005_money'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('what', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='money',
            name='date',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='money',
            name='what',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='paids.currency'),
        ),
    ]

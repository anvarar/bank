# Generated by Django 5.0.1 on 2024-03-03 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0009_alter_balance_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='balance',
            field=models.FloatField(default=0),
        ),
    ]

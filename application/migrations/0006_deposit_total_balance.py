# Generated by Django 5.0.1 on 2024-03-02 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_remove_deposit_total_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='total_balance',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]

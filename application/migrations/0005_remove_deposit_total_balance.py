# Generated by Django 5.0.1 on 2024-03-02 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_deposit_total_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deposit',
            name='total_balance',
        ),
    ]

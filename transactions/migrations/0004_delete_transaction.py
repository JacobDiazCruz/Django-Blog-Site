# Generated by Django 2.1.2 on 2018-10-25 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_remove_transaction_total_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]

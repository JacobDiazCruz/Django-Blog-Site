# Generated by Django 2.1.2 on 2018-10-25 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
    ]
# Generated by Django 3.1.4 on 2020-12-23 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0004_remove_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

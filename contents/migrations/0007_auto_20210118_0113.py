# Generated by Django 3.1.5 on 2021-01-18 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0006_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='gift_code',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_checkout_key',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(default='', max_length=256),
        ),
    ]
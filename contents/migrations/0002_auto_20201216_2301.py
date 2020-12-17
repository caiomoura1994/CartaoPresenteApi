# Generated by Django 3.1.3 on 2020-12-17 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='medium',
            field=models.ImageField(blank=True, null=True, upload_to='productsImages/medium'),
        ),
        migrations.AlterField(
            model_name='image',
            name='original',
            field=models.ImageField(blank=True, null=True, upload_to='productsImages/original'),
        ),
        migrations.AlterField(
            model_name='image',
            name='small',
            field=models.ImageField(blank=True, null=True, upload_to='productsImages/small'),
        ),
    ]

# Generated by Django 3.2.9 on 2023-04-22 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.CharField(max_length=100)),
                ('product_description', models.TextField()),
                ('product_image', models.ImageField(upload_to='')),
                ('product_image_alt', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travel_name', models.CharField(max_length=100)),
                ('travel_price', models.CharField(max_length=100)),
                ('travel_shotr_description', models.CharField(max_length=500)),
                ('travel_extended_description', models.TextField()),
                ('travel_image', models.ImageField(upload_to='')),
                ('travel_image_alt', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Travel',
                'verbose_name_plural': 'Travels',
            },
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-01 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network_links', '0002_alter_product_options_alter_factory_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factory',
            name='email',
            field=models.EmailField(max_length=200),
        ),
    ]

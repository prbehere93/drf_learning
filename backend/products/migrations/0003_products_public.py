# Generated by Django 4.0.3 on 2022-03-16 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]

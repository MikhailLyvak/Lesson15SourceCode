# Generated by Django 5.0.1 on 2024-02-08 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_to_buy_list', '0005_item_bought_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price_in_future',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
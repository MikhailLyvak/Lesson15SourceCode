# Generated by Django 5.0.1 on 2024-02-08 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_to_buy_list', '0004_item_is_bought'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='bought_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]

# Generated by Django 5.0.1 on 2024-02-08 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_to_buy_list', '0002_alter_item_discription'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
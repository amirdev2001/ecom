# Generated by Django 3.2 on 2022-12-09 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_order_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='item',
        ),
    ]
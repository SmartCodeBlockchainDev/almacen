# Generated by Django 3.0.8 on 2020-08-09 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_order_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.0.8 on 2020-08-06 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20200806_0232'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
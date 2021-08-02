# Generated by Django 3.0.8 on 2020-09-08 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20200908_0104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(blank=True, max_length=100, null=True)),
                ('sign', models.ImageField(blank=True, null=True, upload_to='signs')),
                ('typemov', models.IntegerField()),
                ('datemov', models.DateTimeField(auto_now_add=True)),
                ('fromemployee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movfromemployees', to='api.Employee')),
                ('toemployee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movtoemployees', to='api.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='DetailMov',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('movement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Movement')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Product')),
            ],
        ),
    ]
# Generated by Django 3.0.4 on 2020-03-15 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalapp', '0005_auto_20200315_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]

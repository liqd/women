# Generated by Django 2.1.5 on 2019-02-17 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legislatures', '0008_legislature_seats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parliamentarygroup',
            name='percentage_women',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]

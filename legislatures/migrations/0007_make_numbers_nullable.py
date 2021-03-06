# Generated by Django 2.1.5 on 2019-02-11 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legislatures', '0006_parliamentarygroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parliamentarygroup',
            name='number_group',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='parliamentarygroup',
            name='number_women',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='parliamentarygroup',
            name='percentage_group',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]

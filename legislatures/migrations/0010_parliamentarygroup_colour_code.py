# Generated by Django 2.1.7 on 2019-02-17 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legislatures', '0009_make_percentage_women_nullable'),
    ]

    operations = [
        migrations.AddField(
            model_name='parliamentarygroup',
            name='colour_code',
            field=models.CharField(default='', max_length=8),
            preserve_default=False,
        ),
    ]
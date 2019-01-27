# Generated by Django 2.1.5 on 2019-01-27 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legislatures', '0004_auto_20190127_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='legislature',
            name='system',
            field=models.CharField(blank=True, choices=[('WE', 'Weimarer Republik'), ('NS', 'Zeit des Nationalsozialismus'), ('VK', 'Volkskammer der DDR'), ('BT', 'Deutscher Bundestag')], max_length=2),
        ),
    ]

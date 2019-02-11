# Generated by Django 2.1.5 on 2019-02-11 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('legislatures', '0005_legislature_system'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParliamentaryGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(choices=[('CDU', 'CDU/CSU'), ('SPD', 'SPD'), ('FDP', 'FDP'), ('GRU', "B'90/die Grünen, früher: Grüne"), ('LIN', 'Linke, früher: PDS'), ('AFD', 'AfD')], max_length=3)),
                ('percentage_women', models.DecimalField(decimal_places=2, max_digits=4)),
                ('number_women', models.IntegerField(blank=True)),
                ('percentage_group', models.DecimalField(blank=True, decimal_places=2, max_digits=4)),
                ('number_group', models.IntegerField(blank=True)),
                ('legislature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legislatures.Legislature')),
            ],
        ),
    ]

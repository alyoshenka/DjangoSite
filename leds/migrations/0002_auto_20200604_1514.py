# Generated by Django 3.0.6 on 2020-06-04 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='led',
            name='board',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='leds.Board'),
        ),
    ]

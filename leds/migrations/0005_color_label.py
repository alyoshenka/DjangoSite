# Generated by Django 3.0.6 on 2020-05-20 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leds', '0004_auto_20200520_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='label',
            field=models.CharField(default='no_label', max_length=20),
        ),
    ]

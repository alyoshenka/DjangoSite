# Generated by Django 3.0.6 on 2020-06-04 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leds', '0002_auto_20200604_1514'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='led',
            constraint=models.CheckConstraint(check=models.Q(index__gte=0), name='leds_LED_index_gte_0'),
        ),
    ]
# Generated by Django 3.0.6 on 2020-05-22 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leds', '0005_color_label'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.PositiveSmallIntegerField(default=8)),
                ('width', models.PositiveSmallIntegerField(default=32)),
                ('label', models.CharField(default='board', max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='led',
            name='index',
            field=models.IntegerField(default=0),
        ),
    ]

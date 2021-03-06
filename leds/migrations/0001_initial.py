# Generated by Django 3.0.6 on 2020-06-04 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(default='no_label', max_length=20)),
                ('r', models.PositiveSmallIntegerField(default=0)),
                ('g', models.PositiveSmallIntegerField(default=0)),
                ('b', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='LED',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(default=0)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leds.Board')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leds.Color')),
            ],
        ),
    ]

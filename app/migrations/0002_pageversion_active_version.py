# Generated by Django 3.2.5 on 2021-07-26 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pageversion',
            name='active_version',
            field=models.PositiveIntegerField(default=1, verbose_name='Активна версія'),
        ),
    ]

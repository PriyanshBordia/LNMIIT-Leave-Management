# Generated by Django 3.2.9 on 2021-11-20 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0002_auto_20211120_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='application',
            name='reschedules_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]

# Generated by Django 2.1.2 on 2018-10-09 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recent_activity',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recent_activity',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]

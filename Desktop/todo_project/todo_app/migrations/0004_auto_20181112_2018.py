# Generated by Django 2.0.6 on 2018-11-12 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_auto_20181112_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work_details',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
    ]

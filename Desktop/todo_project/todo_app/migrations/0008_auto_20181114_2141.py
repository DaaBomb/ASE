# Generated by Django 2.0.6 on 2018-11-14 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0007_people_project_work_details'),
    ]

    operations = [
        migrations.DeleteModel(
            name='people_project',
        ),
        migrations.DeleteModel(
            name='work_details',
        ),
    ]
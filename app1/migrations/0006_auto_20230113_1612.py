# Generated by Django 3.2 on 2023-01-13 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20230112_2353'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='employee',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='date_updated',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='is_active',
        ),
    ]

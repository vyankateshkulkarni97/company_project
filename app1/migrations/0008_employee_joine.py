# Generated by Django 3.2 on 2023-01-14 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_employee_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Joine',
            field=models.BooleanField(default=True),
        ),
    ]

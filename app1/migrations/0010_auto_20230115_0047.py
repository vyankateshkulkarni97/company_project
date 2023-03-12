# Generated by Django 3.2 on 2023-01-14 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_employeeform'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeeform',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='employeeform',
            old_name='Age',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='employeeform',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='employeeform',
            old_name='Mobile_num',
            new_name='mobile_num',
        ),
        migrations.RenameField(
            model_name='employeeform',
            old_name='Name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='employeeform',
            name='Is_joined',
        ),
        migrations.AddField(
            model_name='employeeform',
            name='Joine',
            field=models.BooleanField(default=True),
        ),
    ]

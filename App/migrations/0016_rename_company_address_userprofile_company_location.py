# Generated by Django 3.2.7 on 2023-02-09 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0015_auto_20230209_1322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='company_address',
            new_name='company_location',
        ),
    ]

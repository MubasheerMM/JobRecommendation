# Generated by Django 3.2.7 on 2023-03-26 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0027_userprofile_admission_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='admission_no',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='reg_no',
            field=models.CharField(blank=True, default=0, max_length=5000),
        ),
    ]

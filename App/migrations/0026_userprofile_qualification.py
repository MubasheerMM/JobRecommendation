# Generated by Django 3.2.7 on 2023-03-25 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0025_alter_saved_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='qualification',
            field=models.CharField(blank=True, max_length=5000),
        ),
    ]
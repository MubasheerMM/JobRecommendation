# Generated by Django 3.2.7 on 2023-01-11 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_chat_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='from_user',
        ),
        migrations.RemoveField(
            model_name='message',
            name='to_user',
        ),
    ]

# Generated by Django 3.2.7 on 2023-01-07 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='userProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='sherlock.jpg', upload_to='profile_pic')),
                ('location', models.CharField(max_length=5000)),
                ('phone', models.CharField(max_length=5000)),
                ('skills', models.CharField(max_length=50000)),
                ('age', models.IntegerField(default=18)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
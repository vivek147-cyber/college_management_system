# Generated by Django 3.1.1 on 2023-03-30 10:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20230330_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='student',
        ),
        migrations.AddField(
            model_name='post',
            name='admin',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

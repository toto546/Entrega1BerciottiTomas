# Generated by Django 4.0.4 on 2022-05-28 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_coder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ligas',
            name='clubes',
        ),
    ]
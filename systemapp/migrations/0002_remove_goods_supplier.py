# Generated by Django 3.0.7 on 2020-06-19 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('systemapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='supplier',
        ),
    ]
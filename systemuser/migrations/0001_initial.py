# Generated by Django 3.0.7 on 2020-06-07 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=20, verbose_name='登录密码')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='用户邮箱')),
            ],
            options={
                'verbose_name': '用户信息',
                'db_table': 'Account',
            },
        ),
    ]
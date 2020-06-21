# Generated by Django 3.0.7 on 2020-06-19 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('systemapp', '0002_remove_goods_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='supplier_goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sup', to='systemapp.Supplier'),
        ),
    ]
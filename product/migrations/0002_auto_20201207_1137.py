# Generated by Django 3.1.3 on 2020-12-07 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='register_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='등록날짜'),
        ),
    ]
# Generated by Django 3.1.3 on 2020-12-12 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scuser', '0002_scuser_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scuser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='비밀번호'),
        ),
    ]

# Generated by Django 3.1.3 on 2020-12-07 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scuser',
            name='level',
            field=models.CharField(choices=[('admin', 'admin'), ('user', 'user')], default='user', max_length=8, verbose_name='등급'),
            preserve_default=False,
        ),
    ]

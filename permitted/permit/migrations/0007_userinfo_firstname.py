# Generated by Django 2.1 on 2018-09-01 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permit', '0006_auto_20180901_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='firstName',
            field=models.CharField(default='', max_length=200),
        ),
    ]

# Generated by Django 2.1 on 2018-09-01 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permit', '0005_remove_userinfo_firstname'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='education',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='profilePic',
            field=models.FileField(default='', upload_to=''),
        ),
    ]

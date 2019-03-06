# Generated by Django 2.0.1 on 2018-04-09 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LBook', '0005_auto_20180409_2345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='lastname',
        ),
        migrations.AddField(
            model_name='signup',
            name='name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='signup',
            name='fathername',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='signup',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]
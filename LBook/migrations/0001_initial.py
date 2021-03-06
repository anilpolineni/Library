# Generated by Django 2.0.1 on 2018-04-09 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookid', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=300)),
                ('authorname', models.CharField(max_length=100)),
                ('dept', models.CharField(choices=[('cse', 'CSE'), ('ece', 'ECE'), ('eee', 'EEE'), ('Mech', 'MECH')], max_length=100)),
                ('edition', models.CharField(max_length=20)),
                ('publisher', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('rollno', models.CharField(max_length=20, unique=True)),
                ('fathername', models.CharField(max_length=300)),
                ('gender', models.CharField(max_length=10)),
                ('mobileno', models.CharField(max_length=12)),
                ('emailId', models.CharField(max_length=100)),
            ],
        ),
    ]

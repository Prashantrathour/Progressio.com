# Generated by Django 4.2.4 on 2023-09-05 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.CharField(default='prashant', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='student',
            name='userID',
            field=models.CharField(default='xyz', max_length=100, unique=True),
        ),
    ]

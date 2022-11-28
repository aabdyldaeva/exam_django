# Generated by Django 4.1.3 on 2022-11-28 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.CharField(default=0, max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='email',
            field=models.CharField(default=0, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='name',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='phone_number',
            field=models.IntegerField(default=0),
        ),
    ]
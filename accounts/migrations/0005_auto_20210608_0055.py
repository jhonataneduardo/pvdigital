# Generated by Django 3.2 on 2021-06-08 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210608_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=120),
        ),
    ]
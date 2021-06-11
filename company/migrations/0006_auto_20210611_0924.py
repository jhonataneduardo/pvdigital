# Generated by Django 3.2 on 2021-06-11 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_andress'),
    ]

    operations = [
        migrations.AddField(
            model_name='andress',
            name='type',
            field=models.CharField(choices=[('residential', 'Residential'), ('other', 'Other')], default='residential', max_length=12),
        ),
        migrations.AddField(
            model_name='employee',
            name='andresses',
            field=models.ManyToManyField(blank=True, null=True, to='company.Andress'),
        ),
    ]

# Generated by Django 3.2 on 2021-06-08 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corporate_function', models.CharField(choices=[('primary', 'Primary'), ('secundary', 'Secundary')], default='primary', max_length=9)),
                ('corporate_name', models.CharField(max_length=120)),
                ('fantasy_name', models.CharField(max_length=120)),
                ('cnpj', models.CharField(max_length=14, verbose_name='CNPJ')),
                ('im', models.CharField(max_length=11, verbose_name='Inscrição Municipal')),
                ('photo', models.ImageField(blank=True, upload_to='companies/%Y/%m/%d/')),
                ('parent_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='socialschool.company')),
            ],
        ),
    ]

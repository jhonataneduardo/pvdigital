# Generated by Django 3.2.4 on 2021-07-30 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0007_group_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=9, verbose_name='Number')),
                ('state', models.CharField(choices=[('draft', 'Draft'), ('reserved', 'Reserved'), ('cancel', 'Cancel'), ('done', 'Done')], max_length=8, verbose_name='State')),
                ('courses', models.ManyToManyField(to='school.Course', verbose_name='Courses')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='school.student', verbose_name='Student')),
            ],
        ),
    ]

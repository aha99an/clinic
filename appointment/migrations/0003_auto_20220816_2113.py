# Generated by Django 2.2.15 on 2022-08-16 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_auto_20220806_0411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='cause',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='diagnose',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='investigation',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='referrer',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='treatment',
        ),
    ]

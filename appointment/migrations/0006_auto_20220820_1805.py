# Generated by Django 2.2.15 on 2022-08-20 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0005_auto_20220818_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='operation',
            field=models.ManyToManyField(null=True, to='operation.Operation'),
        ),
    ]

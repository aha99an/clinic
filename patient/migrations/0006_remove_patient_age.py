# Generated by Django 2.1.5 on 2022-08-06 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0005_patient_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='age',
        ),
    ]
# Generated by Django 4.1.2 on 2022-10-22 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0027_alter_patient_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='birthdate',
            field=models.DateField(blank=True),
        ),
    ]
# Generated by Django 2.2.15 on 2022-08-23 18:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0019_auto_20220823_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='birthdate',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(default='asa', max_length=255),
            preserve_default=False,
        ),
    ]

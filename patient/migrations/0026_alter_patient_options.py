# Generated by Django 4.1.2 on 2022-10-10 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0025_alter_attachment_patient'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient',
            options={'ordering': ('name',)},
        ),
    ]

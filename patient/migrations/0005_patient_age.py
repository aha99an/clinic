# Generated by Django 2.1.5 on 2022-08-06 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_auto_20220806_0447'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='age',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
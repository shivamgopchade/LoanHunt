# Generated by Django 4.0.4 on 2022-05-11 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BankProfile', '0006_alter_bank_profile_cibil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank_profile',
            name='CUR',
            field=models.FloatField(null=True),
        ),
    ]

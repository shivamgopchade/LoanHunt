# Generated by Django 4.0.4 on 2022-05-11 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BankProfile', '0004_alter_bank_profile_bank_alter_bank_profile_ctc'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank_profile',
            name='CIBIL',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='bank_profile',
            name='CUR',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='bank_profile',
            name='Credit_duration',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='bank_profile',
            name='DUE',
            field=models.IntegerField(null=True),
        ),
    ]
# Generated by Django 4.0.4 on 2022-05-10 12:20

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='loans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied_date', models.DateTimeField(default=datetime.datetime.now)),
                ('accepted_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.BooleanField(default=False)),
                ('amt', models.IntegerField()),
                ('tenure', models.IntegerField()),
                ('interest', models.DecimalField(decimal_places=2, max_digits=4)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant_user', to=settings.AUTH_USER_MODEL)),
                ('lender', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lender_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

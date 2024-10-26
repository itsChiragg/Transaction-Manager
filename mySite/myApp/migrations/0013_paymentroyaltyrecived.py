# Generated by Django 5.0.8 on 2024-08-14 21:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0012_remove_paymentroyalty_payment_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentRoyaltyRecived',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateField()),
                ('fisherman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.royaltyfisherman')),
            ],
        ),
    ]

# Generated by Django 5.0.8 on 2024-08-28 15:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0016_advance_manager_paymentroyaltyrecived_manager'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PaymentRoyaltyRecived',
            new_name='PaymentRoyaltyReceived',
        ),
        migrations.CreateModel(
            name='OwnerToManagerTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.manager')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.owner')),
            ],
        ),
    ]

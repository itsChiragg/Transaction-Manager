# Generated by Django 5.0.8 on 2024-08-16 15:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0013_paymentroyaltyrecived'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentroyalty',
            name='catch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myApp.catchroyalty'),
        ),
    ]

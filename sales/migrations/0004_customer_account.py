# Generated by Django 5.1.4 on 2024-12-11 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_customer_email_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='account',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
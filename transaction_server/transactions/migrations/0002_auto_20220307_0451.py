# Generated by Django 3.2.12 on 2022-03-07 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='cryptokey',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=24, null=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='quoteServerTime',
            field=models.DecimalField(decimal_places=2, max_digits=24, null=True),
        ),
    ]

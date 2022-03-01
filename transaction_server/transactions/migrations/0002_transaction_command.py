# Generated by Django 3.2.12 on 2022-03-01 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='command',
            field=models.CharField(choices=[('ADD', 'Add'), ('QUOTE', 'Quote'), ('BUY', 'Buy'), ('COMMIT_BUY', 'Commit Buy'), ('CANCEL_BUY', 'Cancel Buy'), ('SELL', 'Sell'), ('COMMIT_SELL', 'Commit Sell'), ('CANCEL_SELL', 'Cancel Sell'), ('SET_BUY_AMOUNT', 'Set Buy Amount'), ('CANCEL_SET_BUY', 'Cancel Set Buy'), ('SET_BUY_TRIGGER', 'Set Buy Trigger'), ('SET_SELL_AMOUNT', 'Set Sell Amount'), ('SET_SELL_TRIGGER', 'Set Sell Trigger'), ('CANCEL_SET_SELL', 'Cancel Set Sell'), ('DUMPLOG', 'Dumplog'), ('DISPLAY_SUMMARY', 'Display Summary')], default='', max_length=16),
            preserve_default=False,
        ),
    ]

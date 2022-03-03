# Generated by Django 3.2.12 on 2022-03-03 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=50)),
                ('funds', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='accounttransaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.user'),
        ),
        migrations.AlterField(
            model_name='addcommand',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.user'),
        ),
        migrations.AlterField(
            model_name='buycommand',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.user'),
        ),
        migrations.AlterField(
            model_name='cancelbuycommand',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.user'),
        ),
        migrations.AlterField(
            model_name='cancelsellcommand',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.user'),
        ),
        migrations.AlterField(
            model_name='cancelsetbuycommand',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.user'),
        ),
        migrations.AlterField(
            model_name='cancelsetsellcommand',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.user'),
        ),
        migrations.AlterField(
            model_name='commitbuycommand',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.user'),
        ),
        migrations.AlterField(
            model_name='commitsellcommand',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.user'),
        ),
        migrations.AlterField(
            model_name='displaysummarycommand',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transactions.user'),
        ),
        migrations.AlterField(
            model_name='dumplogcommand',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transactions.user'),
        ),
        migrations.AlterField(
            model_name='quotecommand',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.user'),
        ),
        migrations.AlterField(
            model_name='sellcommand',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.user'),
        ),
        migrations.AlterField(
            model_name='setbuyamountcommand',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.user'),
        ),
        migrations.AlterField(
            model_name='setbuytriggercommand',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.user'),
        ),
        migrations.AlterField(
            model_name='setsellamountcommand',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.user'),
        ),
        migrations.AlterField(
            model_name='setselltriggercommand',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.user'),
        ),
    ]
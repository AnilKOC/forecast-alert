# Generated by Django 2.1.15 on 2021-01-23 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock_prices',
            name='f_day',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock_prices',
            name='price_close',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock_prices',
            name='s_day',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock_prices',
            name='t_day',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stocks_list',
            name='f_day',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stocks_list',
            name='s_day',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stocks_list',
            name='t_day',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stocks_list',
            name='value',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
# Generated by Django 2.0.6 on 2018-06-16 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0003_auto_20180614_1913'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rpsprepare',
            options={'verbose_name': 'RPS基础'},
        ),
        migrations.AlterUniqueTogether(
            name='rps',
            unique_together={('code', 'tradedate')},
        ),
    ]

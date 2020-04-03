# Generated by Django 3.0.4 on 2020-04-01 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20200401_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfilemodel',
            name='finish',
            field=models.BooleanField(default=False, verbose_name='거래 완료 여부'),
        ),
        migrations.AddField(
            model_name='uploadfilemodel',
            name='trade_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='거래 시작일'),
        ),
    ]
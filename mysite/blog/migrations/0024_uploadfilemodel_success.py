# Generated by Django 3.0.4 on 2020-04-02 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20200402_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfilemodel',
            name='success',
            field=models.BooleanField(default=False, verbose_name='거래 성사여부'),
        ),
    ]

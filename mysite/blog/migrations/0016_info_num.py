# Generated by Django 3.0.4 on 2020-03-31 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_check_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='num',
            field=models.IntegerField(blank=True, null=True, verbose_name='거래항목'),
        ),
    ]

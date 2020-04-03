# Generated by Django 3.0.4 on 2020-03-31 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_uploadfilemodel_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='check',
            name='photoname',
            field=models.CharField(default='', max_length=200, verbose_name='파일명'),
        ),
        migrations.AlterField(
            model_name='uploadfilemodel',
            name='filename',
            field=models.CharField(default='', max_length=200, verbose_name='파일명'),
        ),
    ]

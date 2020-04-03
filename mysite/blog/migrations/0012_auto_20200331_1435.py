# Generated by Django 3.0.4 on 2020-03-31 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='addition',
            field=models.TextField(null=True, verbose_name='참고목록'),
        ),
        migrations.AlterField(
            model_name='info',
            name='address',
            field=models.TextField(null=True, verbose_name='주소'),
        ),
        migrations.AlterField(
            model_name='info',
            name='addressnum',
            field=models.TextField(null=True, verbose_name='우편번호'),
        ),
        migrations.AlterField(
            model_name='info',
            name='detailaddress',
            field=models.TextField(null=True, verbose_name='상세주소'),
        ),
        migrations.AlterField(
            model_name='info',
            name='request',
            field=models.TextField(null=True, verbose_name='주의 사항'),
        ),
    ]
# Generated by Django 3.0.4 on 2020-03-25 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='', verbose_name='제품사진')),
                ('material_name', models.CharField(max_length=100, verbose_name='이름')),
                ('price', models.IntegerField(default=0, verbose_name='가격')),
                ('explain', models.TextField(blank=True, verbose_name='제품설명')),
                ('inputmoney', models.BooleanField(default=False, verbose_name='입금여부')),
                ('delivery', models.BooleanField(default=False, verbose_name='배송여부')),
            ],
        ),
    ]

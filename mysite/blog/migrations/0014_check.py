# Generated by Django 3.0.4 on 2020-03-31 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200331_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='check',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='', verbose_name='배송사진')),
            ],
        ),
    ]

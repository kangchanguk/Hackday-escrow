# Generated by Django 3.0.4 on 2020-03-29 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_product_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='')),
                ('file', models.FileField(null=True, upload_to='')),
            ],
        ),
    ]

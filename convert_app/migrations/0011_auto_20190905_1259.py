# Generated by Django 2.2.4 on 2019-09-05 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convert_app', '0010_auto_20190905_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graymodel',
            name='gray_image',
            field=models.ImageField(default='output/gray/gray.jpg', upload_to=''),
        ),
    ]

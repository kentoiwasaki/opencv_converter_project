# Generated by Django 2.2.4 on 2019-09-02 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convert_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graymodel',
            name='gray_image',
            field=models.ImageField(default='gray/gray.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='graymodel',
            name='image',
            field=models.ImageField(default='defo', upload_to='gray/'),
        ),
    ]

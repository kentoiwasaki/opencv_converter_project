# Generated by Django 2.2.4 on 2019-09-03 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convert_app', '0005_animemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='MosaicModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/')),
                ('mosaic_image', models.ImageField(default='mosaic/mosaic.jpg', upload_to='')),
            ],
        ),
    ]
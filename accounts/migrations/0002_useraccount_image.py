# Generated by Django 3.2.9 on 2021-11-28 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='画像'),
        ),
    ]

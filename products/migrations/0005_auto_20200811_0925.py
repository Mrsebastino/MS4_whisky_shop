# Generated by Django 3.1 on 2020-08-11 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200811_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prerelease',
            name='pre_release',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]

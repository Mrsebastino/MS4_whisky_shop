# Generated by Django 3.1 on 2020-08-12 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200811_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pre_release',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='PreRelease',
        ),
    ]

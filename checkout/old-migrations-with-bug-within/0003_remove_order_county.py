# Generated by Django 3.1 on 2020-08-21 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20200821_1007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='county',
        ),
    ]

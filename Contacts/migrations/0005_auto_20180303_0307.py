# Generated by Django 2.0.2 on 2018-03-03 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contacts', '0004_auto_20180303_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(),
        ),
    ]

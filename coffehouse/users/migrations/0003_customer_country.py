# Generated by Django 2.1.2 on 2018-11-06 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20181102_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='country',
            field=models.CharField(default=' ', max_length=40),
        ),
    ]
# Generated by Django 2.1.2 on 2018-10-14 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, max_length=4)),
                ('quantity', models.IntegerField()),
                ('note', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, max_length=4)),
                ('quantity', models.IntegerField()),
                ('note', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('processed', models.BooleanField()),
                ('note', models.CharField(max_length=255, null=True)),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drinks', to='orders.Drink')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foods', to='orders.Food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

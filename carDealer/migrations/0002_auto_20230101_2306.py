# Generated by Django 3.1.7 on 2023-01-01 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carDealer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='sold',
        ),
        migrations.AlterField(
            model_name='item',
            name='suspension',
            field=models.CharField(max_length=50),
        ),
    ]

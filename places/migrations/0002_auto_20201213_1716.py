# Generated by Django 3.1.4 on 2020-12-13 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='address',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='place',
            name='maps_url',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='place',
            name='place_id',
            field=models.CharField(max_length=100),
        ),
    ]

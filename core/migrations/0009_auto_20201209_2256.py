# Generated by Django 3.1.2 on 2020-12-09 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_oder'),
    ]

    operations = [
        migrations.AddField(
            model_name='oder',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='oder',
            name='phone',
            field=models.CharField(default='', max_length=20),
        ),
    ]

# Generated by Django 3.0.6 on 2020-05-20 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0005_auto_20200520_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sinquote',
            name='quote',
            field=models.TextField(unique=True),
        ),
    ]

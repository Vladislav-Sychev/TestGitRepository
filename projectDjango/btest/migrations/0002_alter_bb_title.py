# Generated by Django 4.2.7 on 2023-11-06 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]

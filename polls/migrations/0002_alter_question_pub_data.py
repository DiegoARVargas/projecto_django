# Generated by Django 3.2 on 2022-07-22 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_data',
            field=models.DateTimeField(verbose_name='data_published'),
        ),
    ]

# Generated by Django 2.2.7 on 2019-12-03 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marriage',
            name='no',
            field=models.IntegerField(),
        ),
    ]

# Generated by Django 2.2.7 on 2019-12-03 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Annoucement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('body', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Annoucement',
            },
        ),
        migrations.CreateModel(
            name='Baptism',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_of_baptism', models.DateField()),
                ('place_of_baptism', models.CharField(max_length=100)),
                ('baptismal_name', models.CharField(max_length=100)),
                ('other_names', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('place_of_birth', models.CharField(max_length=100)),
                ('hometown', models.CharField(max_length=100)),
                ('name_of_parents', models.CharField(max_length=100)),
                ('solenm_or_private', models.CharField(max_length=100)),
                ('name_of_God_parents', models.CharField(max_length=100)),
                ('name_of_minister', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'baptism',
            },
        ),
        migrations.CreateModel(
            name='Marriage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=100)),
                ('name_of_groom', models.CharField(max_length=100)),
                ('name_of_bride', models.CharField(max_length=100)),
                ('groom_Town', models.CharField(max_length=100)),
                ('bride_Town', models.CharField(max_length=100)),
                ('groom_parent', models.CharField(max_length=200)),
                ('bride_parent', models.CharField(max_length=200)),
                ('assisting_priest', models.CharField(max_length=100)),
                ('groom_witnesses', models.CharField(max_length=100)),
                ('bride_witnesses', models.CharField(max_length=100)),
                ('date_of_marriage', models.DateField()),
                ('remark', models.CharField(default='none', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'marriage ',
            },
        ),
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=200)),
                ('entrace_antiphon', models.TextField()),
                ('opening_prayers', models.TextField()),
                ('first_reading_title', models.CharField(max_length=200)),
                ('first_reading_subtitle', models.CharField(max_length=200)),
                ('first_reading_body', models.TextField()),
                ('responsorial_psalm_title', models.CharField(max_length=200)),
                ('responsorial_psalm_subtitle', models.CharField(max_length=200)),
                ('responsorial_psalm_body', models.TextField()),
                ('second_reading_title', models.CharField(max_length=200)),
                ('second_reading_subtitle', models.CharField(max_length=200)),
                ('second_reading_body', models.TextField()),
                ('gospel_acclamation_title', models.CharField(max_length=200)),
                ('gospel_acclamation_body', models.TextField()),
                ('gospel_title', models.CharField(max_length=200)),
                ('gospel_subtitle', models.CharField(max_length=200)),
                ('gospel', models.TextField()),
                ('prayer_over_the_offerings', models.TextField()),
                ('communion_antiphon', models.TextField()),
                ('prayer_after_communion', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Reading',
            },
        ),
    ]

# Generated by Django 4.1.1 on 2022-09-24 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initial_comm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='adres',
            field=models.CharField(default='адрес не установлен', max_length=50, verbose_name='adres'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='spec',
            field=models.CharField(max_length=20, verbose_name='spec'),
        ),
    ]
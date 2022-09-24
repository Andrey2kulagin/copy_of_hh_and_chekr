# Generated by Django 4.1.1 on 2022-09-24 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initial_comm', '0003_resume_gender_alter_resume_adres'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='age',
            field=models.IntegerField(default=18, verbose_name='age'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='gender',
            field=models.CharField(choices=[('ж', 'ж'), ('м', 'м')], default='', max_length=1, verbose_name='gender'),
        ),
    ]
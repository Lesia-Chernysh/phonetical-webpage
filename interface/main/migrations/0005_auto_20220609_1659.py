# Generated by Django 3.2.13 on 2022-06-09 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20220609_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='informationaboutconsonants',
            name='palatalization',
            field=models.TextField(default='', verbose_name='ступінь палаталізації'),
        ),
        migrations.AddField(
            model_name='informationaboutconsonants',
            name='way_of_articulation',
            field=models.TextField(default='', verbose_name='спосіб артикуляції'),
        ),
    ]

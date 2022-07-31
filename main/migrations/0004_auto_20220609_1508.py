# Generated by Django 3.2.13 on 2022-06-09 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220529_2346'),
    ]

    operations = [
        migrations.CreateModel(
            name='InformationAboutConsonants',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('sound', models.CharField(max_length=5, verbose_name='звук')),
                ('place_of_articulation', models.TextField(default='', verbose_name='місце артикуляції')),
                ('description', models.TextField(verbose_name='опис вимови')),
                ('image', models.ImageField(upload_to='media', verbose_name='ілюстрація вимови')),
                ('documents', models.FileField(default='', upload_to='documents/')),
            ],
        ),
        migrations.RenameModel(
            old_name='InformationAboutSounds',
            new_name='InformationAboutVowels',
        ),
    ]

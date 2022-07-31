from django.db import models


# Create your models here.
class InformationAboutVowels(models.Model):
    id = models.AutoField('id', primary_key=True)
    sound = models.CharField('звук', max_length=5)
    row = models.TextField('ряд', default='')
    description = models.TextField('опис вимови')
    image = models.ImageField('ілюстрація вимови', upload_to="media")
    audio = models.FileField(upload_to='documents/', default='')


class InformationAboutConsonants(models.Model):
    id = models.AutoField('id', primary_key=True)
    sound = models.CharField('звук', max_length=6)
    place_of_articulation = models.TextField('місце артикуляції', default='')
    way_of_articulation = models.TextField('спосіб артикуляції', default='')
    palatalization = models.TextField('ступінь палаталізації', default='')
    description = models.TextField('опис вимови')
    image = models.ImageField('ілюстрація вимови', upload_to="media")
    audio = models.FileField(upload_to='documents/', default='')

    def __str__(self):
        return self.sound

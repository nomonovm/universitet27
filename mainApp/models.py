from django.db import models

class University(models.Model):
    nom = models.CharField(max_length=255)
    class Yonalish(models.Model):
        yonalish1 = models.CharField(max_length=222)
        yonalish2 = models.CharField(max_length=222)
        yonalish3 = models.CharField(max_length=222)
        yonalish4 = models.CharField(max_length=222)
        yonalish5 = models.CharField(max_length=222)
        yonalish6 = models.CharField(max_length=222)
        yonalish7 = models.CharField(max_length=222)
    class Talaba(models.Model):
        yonalish1 = models.PositiveSmallIntegerField()
    class Ustoz(models.Model):
        ustoz = models.CharField(max_length=222)

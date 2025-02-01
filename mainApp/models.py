from django.db import models

class Yonalish(models.Model):
    nom = models.CharField(max_length=255)
    aktiv = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural="Yonalishlar"
    def __str__(self):
        return self.nom

class Fan(models.Model):
    nom = models.CharField(max_length=255)
    yonalish = models.ForeignKey(Yonalish, on_delete=models.CASCADE)
    asosiy = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural="Fanlar"
    def __str__(self):
        return self.nom

class Ustoz(models.Model):
    DARAJA_CHOICES = [
        ('Bakalavr', 'Bakalavr'),
        ('Magistr', 'Magistr'),
        ('PhD', 'PhD'),
        ('DSc', 'DSc'),
    ]

    ism = models.CharField(max_length=255)
    jins = models.CharField(max_length=10, choices=[('Erkak', 'Erkak'), ('Ayol', 'Ayol')])
    yosh = models.PositiveIntegerField()
    daraja = models.CharField(max_length=50, choices=DARAJA_CHOICES)
    fan = models.ForeignKey(Fan, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural="Ustozlar"
    def __str__(self):
        return self.ism

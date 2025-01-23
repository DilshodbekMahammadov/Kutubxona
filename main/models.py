from django.db import models
from django.db.models import PositiveSmallIntegerField


class Muallif(models.Model):
    JINS_CHOISES = (
        ('Erkak','Erkak'),
        ('Ayol','Ayol'),
    )
    ism = models.CharField(max_length=100)
    davlat = models.CharField(max_length=100)
    kitob_soni = models.PositiveSmallIntegerField(blank=True, null=True)
    t_sana = models.DateField(blank=True, null=True)
    tirik = models.BooleanField(default=False)
    jins = models.CharField(max_length=10, choices=JINS_CHOISES, default='Erkak')

    def __str__(self):
        return self.ism
    class Meta:
        verbose_name_plural = 'Mualliflar'

class Kitob(models.Model):
    nom = models.CharField(max_length=255)
    annotatsiya = models.TextField(blank=True, null=True)
    janr = models.CharField(max_length=200)
    sahifa = models.PositiveIntegerField()
    muallif = models.ForeignKey(Muallif, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nom
    class Meta:
        verbose_name_plural = 'Kitoblar'

class Kutubxonachi(models.Model):
    ISH_VAQTI_CHOISES = (
        ('8:00 - 13:00','8:00 - 13:00'),
        ('13:00 - 18:00', '13:00 - 18:00'),
    )
    ism = models.CharField(max_length=250)
    ish_vaqti = models.CharField(max_length=100, choices=ISH_VAQTI_CHOISES, default='8:00 - 13:00')

    def __str__(self):
        return self.ism
    class Meta:
        verbose_name_plural = 'Kutubxonachilar'

class Talaba(models.Model):
    ism = models.CharField(max_length=255)
    kurs = PositiveSmallIntegerField(default=1)
    guruh = models.CharField(max_length=100)
    yosh = models.PositiveSmallIntegerField(default=18)
    kitob_soni = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return  self.ism
    class Meta:
        verbose_name_plural = 'Talabalar'

class Record(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.SET_NULL, null=True)
    kitob = models.ForeignKey(Kitob, on_delete=models.SET_NULL, null=True)
    kutubxonachi = models.ForeignKey(Kutubxonachi, on_delete=models.SET_NULL, null=True)
    olingan_sana = models.DateTimeField(auto_now_add=True)
    qaytarilgan_sana = models.DateTimeField(blank=True, null=True)
    qaytardi = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.talaba}-{self.kutubxonachi}-{self.kitob}'
    class Meta:
        verbose_name_plural = 'Recordlar'
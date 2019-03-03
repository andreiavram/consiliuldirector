from django.db import models

class Decont(models.Model):
    RON = 1
    EUR = 2
    USD = 3
    HUF = 4

    VALUTE = (
        (RON, "RON"),
        (EUR, "EUR"),
        (USD, "USD"),
        (HUF, "HUF"),
    )

    titular = models.CharField(max_length=255, help_text="Nume și prenume")
    activitatea = models.CharField(max_length=1024)
    centrul_local = models.CharField(max_length=1024, null=True, blank=True)
    perioada_start = models.DateField()
    perioada_stop = models.DateField()
    data_decont = models.DateTimeField()
    valuta = models.CharField(choices=VALUTE)


class LinieAvans(models.Model):
    decont = models.ForeignKey(Decont, on_delete=models.CASCADE)
    document_plata = models.CharField(max_length=255, help_text="Felul și numărul documentului de plată")
    data = models.DateField()
    valoarea = models.FloatField()


class LinieDecont(models.Model):
    BON_FISCAL = 1
    CHITANTA = 2
    BILET_INTRARE = 3
    BILET_TRANSPORT = 4
    TICHET = 5

    TIPURI_DOCUMENT = (
        (BON_FISCAL, "Bon Fiscal"),
        (CHITANTA, "Chitanță"),
        (BILET_INTRARE, "Bilet intrare"),
        (BILET_TRANSPORT, "Bilet transport"),
        (TICHET, "Tichet")
    )

    decont = models.ForeignKey(Decont, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    descriere_cheltuieli = models.CharField(max_length=1024, help_text="Descriere cheltuieli")
    furnizor = models.CharField(max_length=255)
    tip_document = models.IntegerField(choices=TIPURI_DOCUMENT)
    numar_document = models.CharField(max_length=255)
    data_document = models.DateField()
    valoare = models.FloatField()

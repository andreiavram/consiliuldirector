from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models, transaction


class ConsiliulDirector(models.Model):
    mandat_inceput = models.IntegerField()
    mandat_sfarsit = models.IntegerField()
    index = models.PositiveIntegerField()

    class Meta:
        verbose_name = "mandat Consiliul Director"
        verbose_name_plural = "mandate Consiliul Director"

    def __str__(self):
        return "{} - {}".format(self.mandat_inceput, self.mandat_sfarsit)


class MembruConsiliulDirector(models.Model):
    membru = models.ForeignKey(User, on_delete=models.CASCADE)
    consiliu_director = models.ForeignKey(ConsiliulDirector, on_delete=models.CASCADE)
    functie = models.CharField(max_length=255, null=True, blank=True)
    poza_profil = models.ImageField(upload_to="uploads/profiles/", null=True, blank=True)

    class Meta:
        verbose_name = "Membru Consiliul Director"
        verbose_name_plural = "Membrii Consiliul Director"

    def __str__(self):
        return "{} ({} - {})".format(self.membru,
                                     self.consiliu_director.mandat_inceput,
                                     self.consiliu_director.mandat_sfarsit)


class Registru(models.Model):
    nume = models.CharField(max_length=255)
    next_number = models.IntegerField(default=1)

    def register_document(self, document, owner=None):
        inregistrare = dict(
            registru=self,
            numar = self.next_number,
            content_type=ContentType.objects.get_for_model(document),
            object_id =document.id,
            owner=owner
        )

        with transaction.atomic():
            intrare_registru = IntrareRegistru.objects.create(**inregistrare)
            self.next_number += 1
            self.save()

        return intrare_registru

    def __str__(self):
        return "{}".format(self.nume)

    class Meta:
        verbose_name_plural = "Registre"
        verbose_name = "Registru"


class IntrareRegistru(models.Model):
    registru = models.ForeignKey(Registru, on_delete=models.CASCADE)
    numar = models.IntegerField()

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    referinta = GenericForeignKey("content_type", "object_id")

    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "Intrari Registru"
        verbose_name = "Intrare Registru"


class Decizie(models.Model):
    DRAFT = 1
    PROPUNERE = 2
    VOT_DESCHIS = 3
    VOT_FINALIZAT = 4
    PROPUNERE_RETRASA = 5

    STATUS = [
        (DRAFT, "Draft"),
        (PROPUNERE, "Propunere"),
        (VOT_DESCHIS, "Vot deschis"),
        (VOT_FINALIZAT, "Vot finalizat"),
        (PROPUNERE_RETRASA, "Propunere retrasă")
    ]

    numar = models.IntegerField(unique=True)
    titlu = models.CharField(max_length=1024)
    text = models.TextField(null=True)

    # pana cand se doreste ca decizia sa fie votata
    deadline_vot = models.DateTimeField(null=True, blank=True)
    data_creata = models.DateTimeField(auto_now_add=True)

    # daca decizia are vot presupus, care este el?
    vot_presupus = models.IntegerField(choices=STATUS, blank=True, null=True)

    # decizia poate sa fie cu vot inceput, vot finalizat
    status = models.IntegerField(choices=STATUS)
    initiator = models.ForeignKey(MembruConsiliulDirector, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "[{}]: {}".format(self.get_status_display(), self.status)

    class Meta:
        verbose_name = "Decizie"
        verbose_name_plural = "Decizii"


class ActiuneDecizie(models.Model):
    PENTRU = 1
    IMPOTRIVA = 2
    ABTINERE = 3
    ABSENTA = 4

    VOT = [
        (PENTRU, "Pentru"),
        (IMPOTRIVA, "Împotrivă"),
        (ABTINERE, "Abținere"),
        (ABSENTA, "Absență")
    ]

    membru = models.ForeignKey(MembruConsiliulDirector, on_delete=models.CASCADE)
    decizie = models.ForeignKey(Decizie, on_delete=models.CASCADE)

    comentariu = models.TextField(null=True, blank=True)
    fisier = models.FileField(upload_to="uploads/documente/", null=True, blank=True)
    fisier_link = models.URLField(null=True, blank=True)
    sursa = models.CharField(max_length=255, null=True, blank=True)
    vot = models.IntegerField(choices=VOT, null=True, blank=True)

    def __str__(self):
        vot = "{} a votat {}".format(self.membru, self.get_vot_display())
        comentariu = "{} a comentat".format(self.membru)

        return vot if self.vot else comentariu


from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Kunde(models.Model):

    benutzer = models.OneToOneField(User, verbose_name=("Benutzer"), on_delete=models.RESTRICT, null=True, blank=True)
    name = models.CharField("Name", max_length=200, null=True, blank=True)
    email = models.CharField("E-Mail", max_length=200, null=True, blank=True)
    
    class Meta:
        verbose_name = ("Kunde")
        verbose_name_plural = ("Kunden")

    def __str__(self):
        return f"{self.benutzer}/{self.name}"

    def get_absolute_url(self):
        return reverse("Kunde_detail", kwargs={"pk": self.pk})


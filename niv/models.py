from django.db import models

# Create your models here.
class Pacient(models.Model):
    #user
    id_pacienta = models.IntegerField()
    ime = models.CharField(max_length=200)
    #priimek = models.CharField(max_length=200)

    def __str__(self):
        return self.ime

class Preiskava(models.Model):
    VRSTE_PREISKAVE = (
        ('D', 'diagnostika'),
        ('CPAP', 'cpap'),
        ('BIPAP', 'bipap'),
    )

    pacient = models.ForeignKey('Pacient')
    vrsta = models.CharField(
        max_length=200,
        choices=VRSTE_PREISKAVE,
                              )

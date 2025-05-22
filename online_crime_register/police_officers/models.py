from django.db import models

# Create your models here.
from crimes.models import BaseClass

from django.contrib.auth.models import User

class PoliceOfficers(BaseClass):

    profile = models.OneToOneField('authentication.Profile',on_delete=models.CASCADE)

    name = models.CharField(max_length=50)

    image = models.ImageField(upload_to='police_officer-image/')

    description = models.TextField()

    def __str__(self):

        return self.name
    
    class Meta:

        verbose_name = 'Police officers'

        verbose_name_plural = 'Police officers'
from django.db import models

# Create your models here.

from crimes.models import BaseClass

class Users(BaseClass):

    
    name = models.CharField(max_length=50)

    email = models.EmailField(max_length=50)

    title = models.CharField(max_length=30)

    description = models.TextField()


    def __str__(self):

        return f'{self.name}--{self.title}'
    
    class Meta:

        verbose_name ='Users'

        verbose_name_plural ='Users'







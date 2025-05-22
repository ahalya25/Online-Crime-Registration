from django.db import models

import uuid

# Create your models here.

class BaseClass(models.Model):

    uuid = models.SlugField(unique=True,default=uuid.uuid4)

    active_status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        abstract = True  

class CategoryChoice(models.TextChoices):

    DRUGS_ABUS_AND_TRAFFICKING = 'Drug Abuse and Trafficking','Drug Abuse and Trafficking'

    SEXUAL_ASSAULT = 'Sexual Assault','Sexual Assault'

    CYBER_CRIME ='Cyber crime','Cyber crime'

    KIDNAPPING = 'Kidnapping','Kidnapping'

    DOMESTIC_VIOLENCE = 'domestic violence','domestic violence'

class StatusChoices(models.TextChoices):

    PENDING =  'pending','pending'

    APPROVED = 'approved','approved'

    REJECTED = 'rejected','rejected'

  
class Crimes(BaseClass):


    reporting_user = models.CharField(max_length=30)

    title = models.CharField(max_length=30)

    reporting_date = models.DateField()

    category = models.CharField(max_length=50,choices=CategoryChoice.choices)

    status = models.CharField(max_length=30,choices=StatusChoices.choices)

    police_officer = models.ForeignKey('police_officers.PoliceOfficers',on_delete=models.SET_NULL,null=True,blank=True)

    

    def __str__(self):

        return f'{self.category}--{self.police_officer}'
    
    class Meta:

        verbose_name ='Crimes'

        verbose_name_plural ='Crimes'

        ordering = ['id']
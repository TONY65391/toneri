from django.db import models

# Create your models here.

class MODELS(models.Model):
    firstname = models.CharField(max_length=500)
    lastname = models.CharField(max_length=500)
    
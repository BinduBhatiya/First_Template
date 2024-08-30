from django.db import models

class myclass(models.Model):
    first_nm = models.CharField(max_length=15)
    last_nm = models.CharField(max_length=15)
# Create your models here.

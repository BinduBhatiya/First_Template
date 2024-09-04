from django.db import models

class myclass(models.Model):
    first_nm = models.CharField(max_length=15)
    last_nm = models.CharField(max_length=15)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

def __str__(self):
    return f"{self.first_nm} {self.last_nm}"
# Create your models here.


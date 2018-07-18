from django.db import models

# Create your models here.

class CGDP(models.Model):
    name = models.TextField()
    code = models.CharField(max_length=10)
    year = models.IntegerField()
    value = models.FloatField()
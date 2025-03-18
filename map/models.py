from django.db import models

class Specialty(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    longitude = models.FloatField()
    latitude = models.FloatField()
    specialty = models.ManyToManyField(Specialty)

    def __str__(self):
        return self.name

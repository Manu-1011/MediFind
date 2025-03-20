from django.db import models

class State(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=100, unique=False)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Specialty(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE, default=1)
    longitude = models.FloatField()
    latitude = models.FloatField()
    specialty = models.ManyToManyField(Specialty)  # Removed on_delete (not supported for ManyToManyField)

    def __str__(self):
        return self.name

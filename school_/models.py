from django.db import models

# Create your models here.

class Class_Madrese(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Dabir(models.Model):
    name = models.CharField(max_length=124)
    age = models.IntegerField()
    Class_Madrese = models.ForeignKey(Class_Madrese, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
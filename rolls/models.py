from django.db import models

# Create your models here.


class Roll(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=20)
    price = models.FloatField()

    def __str__(self):
        return self.name

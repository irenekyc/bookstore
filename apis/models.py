from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(null=True)
    category = models.CharField(max_length=100, default="N/A")
    price = models.FloatField(default=0)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)], null=True)
    num_reviews = models.IntegerField(default=0)
    availablility = models.BooleanField(default=True)
    thumbnail = models.CharField(max_length = 300, default="")

    def __str__(self):
        return self.title



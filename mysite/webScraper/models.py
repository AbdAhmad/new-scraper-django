from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self) -> str:
        return self.title

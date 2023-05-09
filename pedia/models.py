from django.db import models

# Create your models here.

class Entry(models.Model):
    userName = models.CharField(max_length=100, default='korada')
    title = models.CharField(max_length=100, primary_key=True)
    body = models.CharField(max_length=10000)

    def __str__(self) -> str:
        return f"{self.title}: {self.body}"



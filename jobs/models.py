from django.db import models

# Create your models here.
class Jobs(models.Model):
    title = models.CharField(max_length=200)
    skill = models.CharField(max_length=200)


def __str__(self):
    return self.title

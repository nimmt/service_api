from django.db import models

# Create your models here.
class Table(models.Model):
    id = models.CharField(primary_key=True, max_length=100)

from django.db import models

class Table(models.Model):
    id = models.CharField(primary_key=True, max_length=100)

class Player(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

"""
Database objects for screener application
"""
from django.db import models

# Create your models here.
class Rule(models.Model):
    """ Holds rule information """
    formula = models.CharField(max_length=100, primary_key=True)
    criteria = models.CharField(max_length=250)

    def __str__(self):
        return self.formula


class Screen(models.Model):
    """ Holds screen information """
    name = models.CharField(max_length=100, primary_key=True)
    description = models.CharField(max_length=250)
    rules = models.ManyToManyField(Rule)

    def __str__(self):
        return self.name

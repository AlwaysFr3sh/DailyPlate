from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class  Recipe(models.Model):
    formattedJSON = models.JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return "Meal:" + self.formattedJSON['title'] + ", User:" + self.user.username


"""
Write relational model for 'Global' recipies
fields:
    foreign key to private recipe table
    number of ratings
    current rating value
"""
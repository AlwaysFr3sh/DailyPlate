from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin




"""
model for user specific recipies
"""
class  Recipe(models.Model):
    formattedJSON = models.JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return "Meal:" + self.formattedJSON['title'] + ", User:" + self.user.username


"""
relational model for 'Global' recipies
fields:
    foreign key to private recipe table
    number of ratings
    current rating value
    !!!untested!!!
"""
class sharedRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    currentRating = models.FloatField(default=0)
    #to calculate rolling average
    numRatings = models.IntegerField(default=0)
    def updateRating(newRating):
        ratingSum = self.currentRating * self.numRatings + newRating
        self.numRatings += 1
        self.currentRating = ratingSum / numRatings
        return currentRating
    def __str__(self):
        return str(self.recipe) + ", Rating:" + self.currentRating

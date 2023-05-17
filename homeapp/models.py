from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from homeapp.utilities import calculate_bmi

#stores relevant information for recipes that have been shared
class sharedDetails(models.Model):
    #to calculate rolling average
    numRatings = models.IntegerField(default=0)
    currentRating = models.FloatField(default=0)
    #function to rate meal. manipulates only values within object, no influence on history table (see recipe.rate())
    def updateRating(self, newRating):
        ratingSum = self.currentRating * self.numRatings + newRating
        self.numRatings += 1
        self.currentRating = ratingSum / self.numRatings
        self.save()
        return self.currentRating
    def __str__(self):
        return "pk:" + str(self.pk) + ", numRatings:" + str(self.numRatings) + ", Rating:" + str(self.currentRating)

class UserSettings(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True) 
    height = models.FloatField(default=179.8) # cm
    weight = models.FloatField(default=84.0) # kg
    dislikedFoods = models.TextField(max_length=1024)
    delim = ','

    def addDislikedFood(self, newDisliked:str):
        self.dislikedFoods += (newDisliked + self.delim)
        self.save()

    def removeDislikedFood(self, value: str):
        self.dislikedFoods.replace((value + self.delim), "")
        self.save()

    def getDislikedFoods(self):
        return self.dislikedFoods.split(self.delim)[:-1]

    def updateHeight(self, newHeight):
        self.height = newHeight
        self.save()

    def updateWeight(self, newWeight):
        self.weight = newWeight
        self.save()

    def getBMI(self):
        return calculate_bmi(self.height, self.weight)

    def __str__(self):
        return f"Height: {self.height}cm Weight: {self.weight}kg Disliked Foods: {self.getDislikedFoods()}"


#MAIN MODEL FOR RECIPE OBJECTS
#major functionality implemented into this class
class  recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipeJSON = models.JSONField()
    sharedDetails = models.ForeignKey(sharedDetails, on_delete=models.SET_NULL, null=True)
    #returns whether this recipe is public
    def shared(self): return self.sharedDetails is not None
    #following methods return False if action cannot be performed

    #performs necessary actions to make recipe 'shared'
    def share(self):
        #check if already shared
        if(self.shared()): return False
        print("INVOKED SHARE:")
        print("\tRecipe: " + self.getTitle())
        details = sharedDetails()
        details.save()
        self.sharedDetails = details
        self.save()
        return True#success
    #performs necessary actions rate this recipe
    def rate(self, user, newRating):
        print("INVOKED RATE:")
        print("\tUser: " + user.username)
        print("\tRecipe: " + self.getTitle())
        print("\tRating: " + str(newRating))
        #if not shared, share first
        if(not self.shared()): 
            print("! Recipe is currently private !")
            self.share()
        #if user has already rated this recipe
        if(ratingHistory.objects.filter(user=user, sharedRecipe=self.sharedDetails).exists()): return False

        self.sharedDetails.updateRating(newRating)
        ratingHistory(ratingGiven=newRating, user=user, sharedRecipe=self.sharedDetails).save()
        return True#success
    #simply get title from JSON field
    def getTitle(self): return self.recipeJSON['title']
    #checks whether 'checkUser' has already given a rating
    def ratedByUser(self, checkUser): return ratingHistory.objects.filter(user=checkUser, sharedRecipe=self.sharedDetails)
    def givenRating(self, user):
        if (self.ratedByUser(user)): 
            return ratingHistory.objects.get(user=user, sharedRecipe=self.sharedDetails).ratingGiven
        else:
            return -1
    def __str__(self):
        rtn = "pk:" + str(self.pk) + ", Title:" + self.getTitle() + ", User:" + self.user.username
        if(self.shared()): rtn += ", sharedDetails: (" + self.sharedDetails.__str__() + ")"
        return rtn

#table to log each time a user rates a recipe
#will be used to create user bespoke openAI prompts
class ratingHistory(models.Model):
    ratingGiven = models.FloatField(default=0, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    sharedRecipe = models.ForeignKey(sharedDetails, on_delete=models.CASCADE, null=False)
    def __str__(self):
        return "pk:" + str(self.pk) + ", user:" + self.user.username + ", recipe:" + recipe.objects.get(sharedDetails=self.sharedRecipe).getTitle()




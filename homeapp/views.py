from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
import sys
from homeapp.api_call_functions.openaiapi import gpt_query
from homeapp.utilities import read_file, construct_prompt
import re
import homeapp.api_call_functions.edamam
from homeapp.api_call_functions.edamam import get_nutritional_info

# Display private and shared recipes
@login_required
def home(request):
  personalRecipes = reversed(recipe.objects.filter(user=request.user))
  globalRecipes = [r for r in recipe.objects.filter() if r.shared()]
  context = {
    "personalRecipes" : personalRecipes,
    "globalRecipes" : globalRecipes,
  }
  return render(request, "home.html", context=context)

# Display single recipe. Requires user to be logged in.
@login_required
def renderRecipe(request, recipeID):
  selectedRecipe=recipe.objects.get(pk=recipeID)
  ratedByUser=selectedRecipe.ratedByUser(checkUser=request.user)
  givenRating=selectedRecipe.givenRating(user=request.user)
  #ratedByUser bool must be parsed here as method cannot be called in DTL as it requires parameters
  context = {
    'recipe':selectedRecipe,
    'ratedByUser':ratedByUser,
    'givenRating':givenRating
  }
  return render(request, "recipe.html", context)



def rateRecipe(request):
  selectedRecipe = recipe.objects.get(pk=request.POST.get('recipeID'))
  newRating = int(request.POST.get('newRating'))
  user = request.user
  print("Attempting rating:")
  print("\tUser: " + user.username)
  print("\tRecipe: " + selectedRecipe.getTitle())
  print("\tRating: " + str(newRating))
  success = selectedRecipe.rate(user=user, newRating=newRating)
  resp={}
  if (success):
    resp['outcome_str'] = 'Recipe has been sucessfully been rated'
  else: resp['outcome_str'] = 'Rating failed. Either user has already rated this meal or the recipe no longer exists.'
  print(resp['outcome_str'])
  return JsonResponse(resp, status=200)

#Recipe generation
def generateRecipe(request):

  # get 5 most recent meals
  prev_meals = recipe.objects.filter(user=request.user).order_by('-id')[:5]
  prev_meals_titles = [meal.getTitle() for meal in prev_meals]

  # get disliked ingredients
  settings = UserSettings.objects.get(user=request.user.pk)

  # construct prompt
  prompt = construct_prompt("dailyplate/prompts/prompt5.txt",
                            disliked_ingredients=settings.getDislikedFoods(), 
                            meal_history=prev_meals_titles, 
                            bmi=settings.getBMI())
  print(prompt)

  # query openai
  system_prompt = "You are a helpful assistant"
  api_key = "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"
  result = gpt_query(prompt, system_prompt, api_key, temperature=1.0)[0]
  #result = read_file("dailyplate/prompts/testresult.txt")
  result = result.replace("\\n", '')
  print(result)
  # strip any text from outside of the json
  begin, end = result.find('{'), result.rfind('}')
  result = result[begin: end+1]
  print(result)
  result=json.loads(result)
  # for ingredient in result.values():
  #   temp = get_nutritional_info(ingredient)

  #   result['ingredients']['kcals'] = (temp['calories'])
  newRecipe=recipe(user=request.user, recipeJSON=result)

  for ingredient_name in result['ingredients'].keys():
    
    result['ingredients'][ingredient_name]['nutrition'] = get_nutritional_info(ingredient_name)


  #print("Nutritional Information:")
    #     print("Calories:", result['calories'])
    #     print("Protein:", result['totalNutrients']['PROCNT']['quantity'], result['totalNutrients']['PROCNT']['unit'])
    #     print("Carbohydrates:", result['totalNutrients']['CHOCDF']['quantity'], result['totalNutrients']['CHOCDF']['unit'])


  
#     {% for ingredient, ingredient_data in recipe.recipeJSON.ingredients.items %}
#       <li> {{ ingredient_data.amount }} {{ ingredient_data.unit }} {{ ingredient }}</li>
#     {% endfor %}

  newRecipe.save()
  resp={
    'title': newRecipe.getTitle(),
    'pk': newRecipe.pk
    }
  return JsonResponse(resp, status=200)







from django import forms
class UserSettingsForm(forms.ModelForm):
  height = forms.DecimalField(
        required=True,
        label='Height (cm)', 
        max_digits=5,
        decimal_places=2,
        max_value=300,
        min_value=0
  )
  weight = forms.DecimalField(
        required=True,
        label='Weight (kg)',
        max_digits=5,
        decimal_places=2,
        max_value=300,
        min_value=0
  )
  dislikedFoods = forms.CharField(
        required=True,
        label='Ingredient Blacklist (enter foods separated by commas):',
        max_length=1024,
        )
  
  class Meta:
    model = UserSettings
    fields = ['height', 'weight', 'dislikedFoods']

  def save(self, settings, commit=True):
    UserSettings = super().save(commit=False)
    settings.dislikedFoods=self.cleaned_data["dislikedFoods"]
    settings.height=self.cleaned_data["height"]
    settings.weight=self.cleaned_data["weight"]
    if commit:
      settings.save()
    return



def renderSettingsPage(request):
  user=request.user
  settings=UserSettings.objects.get(user=user)
  initial_values = {
      'height': settings.height,
      'weight': settings.weight,
      'dislikedFoods': settings.dislikedFoods
  }

  if request.method == 'POST':
    form = UserSettingsForm(request.POST)
    if form.is_valid():
      settings = UserSettings.objects.get(user=request.user)
      form.save(settings=settings)
      # Redirect or do something else
  else:
    form = UserSettingsForm(initial=initial_values)
  return render(request, "settings.html", {'form':form})

"""
def renderSettingsPage(request):
  #get current settings to display

  context={}
  return render(request, "settings.html", context)
"""


def test_recipe_view(request):
  context = {
    "title" : "<recipe title>",
    "ingredients" : {
      "<ingredient 1 name>" : {
        "amount" : "<amount>",
        "unit" : "<unit of measurement>",
        "price" : "<price>"}
      },
    "instructions" : [
      "<step 1>",
      "<step n>"
    ]
  }
  return render(request, "recipe.html", context)


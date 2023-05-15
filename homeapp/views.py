from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse



  

# Display private and shared recipes
@login_required
def home(request):
  personalRecipes = recipe.objects.filter(user=request.user)
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
import json
import sys
from homeapp.api_call_functions.openaiapi import gpt_query
from homeapp.utilities import read_file, construct_prompt
def generateRecipe(request):
  api_key = read_file("newopenaikey")
  prompt = construct_prompt("dailyplate/prompts/prompt4.txt", [])
  system_prompt = "You are a helpful assistant"
  result = gpt_query(prompt, system_prompt, api_key)[0]
  #result = read_file("dailyplate/prompts/testresult.txt")
  result = result.replace("\\n", '')
  print(result)
  result=json.loads(result)
  newRecipe=recipe(user=request.user, recipeJSON=result)
  newRecipe.save()
  resp={
    'title': newRecipe.getTitle(),
    'pk': newRecipe.pk
    }
  return JsonResponse(resp, status=200)










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


from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



"""
#TODO: move this to different file idk which file tho
def get_user_recipes(username: str) -> list[Recipe]:
  user = User.objects.get(username=username)
  recipes = Recipe.objects.filter(user=user)
  [print(recipe.id) for recipe in recipes]
  recipes_json = [recipe.formattedJSON for recipe in recipes]
  # incredibly scuffed
  for recipe_json, recipe in zip(recipes_json, recipes):
    recipe_json["id"] = recipe.id
  return  {"recipes" : recipes_json }


# Could be optimised to only return recipe objects in query
def get_global_recipes() -> list[sharedRecipe]:
  sRecipes = sharedRecipe.objects.filter()
  [print(sRecipe.id) for sRecipe in sRecipes]
  sRecipes_json = [sRecipe.formattedJSON() for sRecipe in sRecipes]
  # incredibly scuffed
  for sRecipes_json, sRecipe in zip(sRecipes_json, sRecipes):
    sRecipes_json["id"] = sRecipe.id
  return  { "sharedRecipes" : sRecipes_json }
"""
#!!!rewritten code above for new model architecture!!!


  

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
  #ratedByUser bool must be parsed here as method cannot be called in DTL as it requires parameters
  context = {
    'recipe':selectedRecipe,
    'ratedByUser':ratedByUser
  }
  return render(request, "recipe.html", context)






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


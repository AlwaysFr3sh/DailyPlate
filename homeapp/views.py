from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

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
def get_global_recipes() -> list[Recipe]:
  sRecipes = sharedRecipe.objects.filter()
  [print(sRecipe.recipe.id) for sRecipe in sRecipes]
  recipes_json = [sRecipe.recipe.formattedJSON for sRecipe in sRecipes]
  # incredibly scuffed
  for recipe_json, sRecipe in zip(recipes_json, sRecipes):
    recipe_json["id"] = sRecipe.recipe.id
  return  {"sharedRecipes" : recipes_json }

  
# Display private and shared recipes
def home(request):
  recipes = get_user_recipes(request.user.username)
  sharedRecipies = get_global_recipes()
  #simple display of global recipes
  #requires implimentation of rating display and submission
  context=recipes
  context.update(sharedRecipies)
  return render(request, "home.html", context=context)
  

# Display single recipe. Requires user to be logged in
@login_required
def recipe(request, id):
  context = Recipe.objects.get(id=id).formattedJSON 
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


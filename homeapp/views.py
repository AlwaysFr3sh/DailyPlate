from django.shortcuts import render
from .models import Recipe
from django.contrib.auth.models import User

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

# Create your views here.
def home(request):
  recipes = get_user_recipes(request.user.username)
  return render(request, "home.html", context=recipes)

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


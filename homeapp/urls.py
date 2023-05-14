
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('test_recipe_view/', views.test_recipe_view, name="testrecipe"),
    path('recipe/<int:recipeID>', views.renderRecipe, name="render_recipe"),
]
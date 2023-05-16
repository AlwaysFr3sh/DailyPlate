
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('test_recipe_view/', views.test_recipe_view, name="testrecipe"),
    path('recipe/<int:recipeID>', views.renderRecipe, name="render_recipe"),
    path('settings', views.renderSettingsPage, name="settings"),
    #No explicitly declared params here.
    #This function is only called through AJAX, so required data is send in request
    path('rate/', views.rateRecipe, name="rate_recipe"),
    path('generate/', views.generateRecipe, name="generate_recipe"),
]
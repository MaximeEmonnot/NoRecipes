from django.urls import path
from .views.views_test_maxime import *
from .views.recipe import *
from .views.ingredient import *

urlpatterns = [
    path("test/", data_list), 

    #urls recettes
    path('add_recipe', add_recipe), 
    path('recipes/', get_all_recipes),
    path('recipes/<str:title>', get_recipe_by_title),
    path('recipes/update/<str:title>', update_recipe),
    path('recipes/delete/<str:title>', delete_recipe),

    #urls ingredients
    path('add_ingredient', add_ingredient), 
    path('ingredients/', get_all_ingredients),
    path('ingredients/<str:title>', get_ingredient_by_title),
    path('ingredients/update/<str:title>', update_ingredient),
    path('ingredients/delete/<str:title>', delete_ingredient)
]

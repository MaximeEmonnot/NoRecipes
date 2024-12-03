from django.urls import path
from .views.views_test_maxime import *
from .views.recipe import *
from .views.ingredient import *
from .views.utensil import *
from .views.category import *
from .views.connector_recipe_category import *
from .views.connector_recipe_ingredient import *
from .views.connector_recipe_utensil import *
from .views.comments import *

urlpatterns = [
    path("test/", data_list), 

    #urls recettes
    path('add_recipe', add_recipe), 
    path('recipes/', get_all_recipes),
    path('recipes/<str:title>', get_recipe_by_title),
    path('recipes/update/<str:title>', update_recipe),
    path('recipes/delete/<str:title>', delete_recipe),
    
    #urls recherche/recommandation
    path('simple_recipe_search/<str:search>', get_recipe_by_simple_search),
    path('advanced_recipe_search/', get_recipe_by_advanced_search),
    path('recommanded_recipes/', get_recommanded_recipes),

    #urls ingredients
    path('add_ingredient', add_ingredient), 
    path('ingredients/', get_all_ingredients),
    path('ingredients/<str:title>', get_ingredient_by_title),
    path('ingredients/update/<str:title>', update_ingredient),
    path('ingredients/delete/<str:title>', delete_ingredient),
    
    #urls Ustensile
    path('add_utensil', add_utensil), 
    path('utensils/', get_all_utensils),
    path('utensils/<str:title>', get_utensil_by_title),
    path('utensils/update/<str:title>', update_utensil),
    path('utensils/delete/<str:title>', delete_utensil),

    #urls Categories
    path('add_category', add_category), 
    path('categories/', get_all_categories),
    path('categories/<str:title>', get_category_by_title),
    path('categories/update/<str:title>', update_category),
    path('categories/delete/<str:title>', delete_category),

    #urls commentaires
    path('comments/add/<str:recipe_title>/', add_comment),
    path('comments/<str:comment_id>/', get_comment),
    path('comments/update/<str:comment_id>/', update_comment),
    path('comments/delete/<str:comment_id>/', delete_comment),
    path('comments/all/<str:recipe_title>/', get_all_comments),

    #urls connexions (relations)
    path('recipes/add_to_category/<str:recipe_title>/<str:category_title>/', add_recipe_to_category),
    path('recipes/remove_from_category/<str:recipe_title>/<str:category_title>/', remove_recipe_from_category),
    path('recipes/by_category/<str:category_title>/', get_recipes_by_category),
    path('categories/by_recipe/<str:recipe_title>/', get_category_by_recipe),

    path('recipes/<str:recipe_title>/ingredients/<str:ingredient_title>/add/', add_ingredient_to_recipe),
    path('recipes/ingredients/<str:recipe_title>', get_ingredients_of_recipe),

    path('recipes/<str:recipe_title>/utensils/<str:ustensile_title>/add/', add_ustensil_to_recipe),
    path('recipes/utensils/<str:recipe_title>', get_utensils_of_recipe),

]

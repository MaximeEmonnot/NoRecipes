from django.urls import path
from .views.views_test_maxime import *
from .views.recipe import *

urlpatterns = [
    path("test/", data_list), 
    path('add_recipe', add_recipe), 
    path('recipes/', get_all_recipes),
    path('recipes/<str:title>', get_recipe_by_title),
    path('recipes/update/<str:title>', update_recipe),
    path('recipes/delete/<str:title>', delete_recipe)
]

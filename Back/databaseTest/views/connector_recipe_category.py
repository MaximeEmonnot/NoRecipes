from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from databaseTest.models import Recipe, Category
import json

from utils import RunCypher, GetDataFromNode

#Ajout d'une recette à une catégorie
@csrf_exempt
def add_recipe_to_category(request, recipe_title, category_title):
    if request.method == "POST":
        try:
            recipe = Recipe.nodes.get(titre=recipe_title)
            category = Category.nodes.get(titre=category_title)
            
            if recipe.categorie.is_connected(category):
                return JsonResponse({"error": "La recette est déjà associée à cette catégorie."}, status=400)
            
            recipe.categorie.connect(category)
            
            return JsonResponse({"message": f"La recette '{recipe_title}' a été associée à la catégorie '{category_title}'."})
        
        except Recipe.DoesNotExist:
            return JsonResponse({"error": "Recette non trouvée."}, status=404)
        except Category.DoesNotExist:
            return JsonResponse({"error": "Catégorie non trouvée."}, status=404)

#Supprimer une recette dans une catégorie
@csrf_exempt
def remove_recipe_from_category(request, recipe_title, category_title):
    if request.method == "DELETE":
        try:
            recipe = Recipe.nodes.get(titre=recipe_title)
            category = Category.nodes.get(titre=category_title)
            
            if not recipe.categorie.is_connected(category):
                return JsonResponse({"error": "La recette n'est pas associée à cette catégorie."}, status=400)

            recipe.categorie.disconnect(category)
            
            return JsonResponse({"message": f"La recette '{recipe_title}' a été dissociée de la catégorie '{category_title}'."})
        
        except Recipe.DoesNotExist:
            return JsonResponse({"error": "Recette non trouvée."}, status=404)
        except Category.DoesNotExist:
            return JsonResponse({"error": "Catégorie non trouvée."}, status=404)

#Récupérer toutes les recettes d'une catégorie
@csrf_exempt
def get_recipes_by_category(request, category_title):
    if request.method == "GET":
        try:
            category = Category.nodes.get(titre=category_title)
            recipes = category.recettes.all()
            
            data = [
                {
                    "titre": recipe.titre,
                    "origine": recipe.origine,
                    "note": recipe.note,
                    "description": recipe.description,
                    "images": recipe.images,
                    "temps_preparation": recipe.temps_preparation,
                    "temps_cuisson": recipe.temps_cuisson,
                    "nombre_personnes": recipe.nombre_personnes
                }
                for recipe in recipes
            ]
            
            return JsonResponse({"recettes": data})
        
        except Category.DoesNotExist:
            return JsonResponse({"error": "Catégorie non trouvée."}, status=404)
            
#Obtenir la catégorie d'une recette
@csrf_exempt
def get_category_by_recipe(request, recipe_title):
    if request.method == "GET":
        try:
            recipe = Recipe.nodes.get(titre=recipe_title)
            
            category = recipe.categorie.single()
            if category is None:
                return JsonResponse({"error": "La recette n'est associée à aucune catégorie."}, status=404)
            
            data = {
                "titre": category.titre,
                "images": category.images
            }
            
            return JsonResponse({"categorie": data})
        
        except Recipe.DoesNotExist:
            return JsonResponse({"error": "Recette non trouvée."}, status=404)

from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from databaseTest.models import Recipe, Ingredient, Contient
import json

from utils import RunCypher, GetDataFromNode

@csrf_exempt
def add_ingredient_to_recipe(request, recipe_title, ingredient_title):
    if request.method == "POST":
        try:
            recipe = Recipe.nodes.get(titre=recipe_title)
            ingredient = Ingredient.nodes.get(titre=ingredient_title)
            
            valid_units = {
                "g": "Grammes",
                "ml": "Millilitres",
                "l": "Litres",
                "cs": "Cuillère à soupe",
                "cc": "Cuillère à café"
            }

            # Données de la requête pour avoir la quantité de l'ingrédient et son unité
            data = json.loads(request.body)
            quantite = data.get("quantite")
            type_unite = data.get("unite")

            if not quantite or not type_unite:
                return JsonResponse({"error": "La quantité et l'unité sont obligatoires."}, status=400)

            if type_unite not in valid_units:
                return JsonResponse({
                    "error": f"Type d'unité invalide. Choisissez parmi : {', '.join(valid_units.keys())}"
                }, status=400)

            # Connecter la recette et l'ingrédient
            recipe.ingredients.connect(ingredient, {
                'quantite': quantite,
                'type_unite': type_unite
            })

            return JsonResponse({
                "message": f"Ingrédient '{ingredient_title}' ajouté à la recette '{recipe_title}'.",
                "quantite": quantite,
                "type_unite": valid_units[type_unite]
            })

        except Recipe.DoesNotExist:
            return JsonResponse({"error": "Recette non trouvée."}, status=404)
        except Ingredient.DoesNotExist:
            return JsonResponse({"error": "Ingrédient non trouvé."}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Données invalides."}, status=400)

@csrf_exempt
def get_ingredients_of_recipe(request, recipe_title):
    if request.method == "GET":
        try:
            recipe = Recipe.nodes.get(titre=recipe_title)
            
            ingredients = []
            for ingredient in recipe.ingredients.all():
                # Récupérer les propriétés de la relation
                rel = recipe.ingredients.relationship(ingredient)
                ingredients.append({
                    "ingredient": ingredient.titre,
                    "quantite": rel.quantite,
                    "type_unite": rel.type_unite
                })

            return JsonResponse({
                "recipe": recipe_title,
                "ingredients": ingredients
            })

        except Recipe.DoesNotExist:
            return JsonResponse({"error": "Recette non trouvée."}, status=404)

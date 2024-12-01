from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from databaseTest.models import Recipe, Utensil, Utilise
import json

from utils import RunCypher, GetDataFromNode

@csrf_exempt
def add_ustensil_to_recipe(request, recipe_title, ustensile_title):
    if request.method == "POST":
        try:
            recipe = Recipe.nodes.get(titre=recipe_title)
            ustensile = Utensil.nodes.get(titre=ustensile_title)

            data = json.loads(request.body)
            nombre = data.get("nombre", 1)

            if not isinstance(nombre, int) or nombre <= 0:
                return JsonResponse({
                    "error": "Le champ 'nombre' doit être un entier positif."
                }, status=400)

            recipe.ustensiles.connect(ustensile, {'nombre': nombre})

            return JsonResponse({
                "message": f"Ustensile '{ustensile_title}' ajouté à la recette '{recipe_title}' avec succès.",
                "nombre": nombre
            })

        except Recipe.DoesNotExist:
            return JsonResponse({"error": "Recette non trouvée."}, status=404)
        except Utensil.DoesNotExist:
            return JsonResponse({"error": "Ustensile non trouvé."}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Données invalides."}, status=400)

@csrf_exempt
def get_utensils_of_recipe(request, recipe_title):
    if request.method == "GET":
        try:
            recipe = Recipe.nodes.get(titre=recipe_title)

            ustensiles = []
            for utensil in recipe.ustensiles.all():
                rel = recipe.ustensiles.relationship(utensil)
                ustensiles.append({
                    "utensil": utensil.titre,
                    "nombre": rel.nombre  
                })

            return JsonResponse({
                "recipe": recipe_title,
                "ustensiles": ustensiles
            })

        except Recipe.DoesNotExist:
            return JsonResponse({"error": "Recette non trouvée."}, status=404)
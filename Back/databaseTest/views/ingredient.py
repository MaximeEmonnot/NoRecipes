from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from databaseTest.models import Ingredient
import json
import os

from utils import RunCypher, GetDataFromNode

# Récupération de tous les ingredient
@csrf_exempt
def get_all_ingredients(request):
    if request.method == "GET":
        ingredients = Ingredient.nodes.all()
        data = [
            {
                "titre": ingredient.titre,
                "images": ingredient.images,
                "prix": ingredient.prix,
                "description": ingredient.description
            }
            for ingredient in ingredients
        ]
        return JsonResponse({"ingredients": data}, safe=False)

# Récupération ingredient par le titre
@csrf_exempt
def get_ingredient_by_title(request, title):
    if request.method == "GET":
        try:
            ingredient = Ingredient.nodes.get(titre=title)
            data = {
               "titre": ingredient.titre,
               "prix": ingredient.prix,
               "description": ingredient.description,
               "images": ingredient.images
            }
            return JsonResponse({"ingredient": data})
        except Ingredient.DoesNotExist:
            return JsonResponse({"error": "Ingrédient non trouvé"}, status=404)

# Ajout de ingredient
@csrf_exempt
def add_ingredient(request):
    if request.method == "POST":
        try: 
            titre = request.POST.get("titre")
            prix = request.POST.get("prix")
            description = request.POST.get("description")
            
            if not all([titre, prix, description]):
                return JsonResponse({"error": "Tous les champs sont requis."}, status=400)

            ingredient = Ingredient(
                titre=titre,
                prix=prix,
                description=description
            )
            ingredient.save()

            # Gestion des fichiers (images)
            images = request.FILES.getlist("images")  
            image_urls = []

            # Chemin vers le répertoire media
            media_path = "media/ingrédients"
            if not os.path.exists(media_path): 
                os.makedirs(media_path)

            for image in images:
                image_name = f"ingrédients/{image.name}"
                image_urls.append(image_name)

                with open(f"media/{image_name}", "wb+") as destination:
                    for chunk in image.chunks():
                        destination.write(chunk)

            # Ajout des images de l'ingrédient
            ingredient.images = image_urls
            ingredient.save()

            return JsonResponse({"message": "Ingrédient créé avec succès", "ingredient_id": ingredient.element_id})

        except Exception as e:
            return JsonResponse({"error": f"Erreur lors de la création de l'ingrédient : {str(e)}"}, status=500)

# Modification ingredient
@csrf_exempt
def update_ingredient(request, title):
    if request.method == "PUT":
        try:
            ingredient = Ingredient.nodes.get(titre=title)
            data = json.loads(request.body)
            
            ingredient.prix = data.get("prix", ingredient.prix)
            ingredient.description = data.get("description", ingredient.description)
            ingredient.images = data.get("images", ingredient.images)
            
            ingredient.save()
            
            return JsonResponse({"message": "Ingrédient mis à jour avec succès"})
        
        except Ingredient.DoesNotExist:
            return JsonResponse({"error": "Ingrédient non trouvé"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Données invalides"}, status=400)

# Suppression ingredient
@csrf_exempt
def delete_ingredient(request, title):
    if request.method == "DELETE":
        try:
            ingredient = Ingredient.nodes.get(titre=title)

            ingredient.delete()
            
            return JsonResponse({"message": "Ingrédient supprimé avec succès"})
        
        except Ingredient.DoesNotExist:
            return JsonResponse({"error": "Ingrédient non trouvé"}, status=404)        


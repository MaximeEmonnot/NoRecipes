from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from databaseTest.models import Category
import json
import os 

from utils import RunCypher, GetDataFromNode

# Récupération de toutes les catégories
@csrf_exempt
def get_all_categories(request):
    if request.method == "GET":
        categories = Category.nodes.all()
        data = [
            {
                "titre": category.titre,
                "images": category.images
            }
            for category in categories
        ]
        return JsonResponse({"Catégories": data}, safe=False)

# Récupération catégorie par le titre
@csrf_exempt
def get_category_by_title(request, title):
    if request.method == "GET":
        try:
            category = Category.nodes.get(titre=title)
            data = {
               "titre": category.titre,
               "images": category.images
            }
            return JsonResponse({"Catégorie": data})
        except Category.DoesNotExist:
            return JsonResponse({"error": "Catégorie non trouvée"}, status=404)

# Ajout d"une catégorie
@csrf_exempt
def add_category(request):
    if request.method == "POST":
        try: 
            titre = request.POST.get("titre")
            
            if not titre:
                return JsonResponse({"error": "Il faut un titre pour la catégorie."}, status=400)

            category = Category(
                titre=titre
            )
            category.save()

            # Gestion des fichiers (images)
            images = request.FILES.getlist("images")  
            image_urls = []

            # Chemin vers le répertoire media
            media_path = "media/catégories"
            if not os.path.exists(media_path): 
                os.makedirs(media_path)

            for image in images:
                image_name = f"catégories/{image.name}"
                image_urls.append(image_name)

                with open(f"media/{image_name}", "wb+") as destination:
                    for chunk in image.chunks():
                        destination.write(chunk)

            # Ajout des images de l'ingrédient
            category.images = image_urls
            category.save()

            return JsonResponse({"message": "Catégorie créée avec succès", "category_id": category.element_id})

        except Exception as e:
            return JsonResponse({"error": f"Erreur lors de la création de la catégorie : {str(e)}"}, status=500)

# Modification catégorie
@csrf_exempt
def update_category(request, title):
    if request.method == "PUT":
        try:
            category = Category.nodes.get(titre=title)
            data = json.loads(request.body)
            category.images = data.get("images", category.images)
            
            category.save()
            
            return JsonResponse({"message": "Catégorie mis à jour avec succès"})
        
        except Category.DoesNotExist:
            return JsonResponse({"error": "Catégorie non trouvée"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Données invalides"}, status=400)

# Suppression Catégorie
@csrf_exempt
def delete_category(request, title):
    if request.method == "DELETE":
        try:
            category = Category.nodes.get(titre=title)

            category.delete()
            
            return JsonResponse({"message": "Catégorie supprimée avec succès"})
        
        except Category.DoesNotExist:
            return JsonResponse({"error": "Catégorie non trouvée"}, status=404)        


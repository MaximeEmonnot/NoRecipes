from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from databaseTest.models import Category
import json

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
            data = json.loads(request.body)
            # Vérification si data est un dictionnaire et pas une liste pour bien gérer la liste des images
            if not isinstance(data, dict):
                return JsonResponse({"error": "Le format est incorrect"}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Données invalides."}, status=400)


        #data = request.POST a utilisé quand le front end sera coder 

        titre = data.get("titre")
        images = data.get("images", "[]")  
        
        if not titre:
            return JsonResponse({"error": "Le titre est obligatoire."}, status=400)

        category = Category(
            titre=titre,
            images=images
        )
        category.save()

        return JsonResponse({"message": "Catégorie créée avec succès", "category_id": category.element_id})

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


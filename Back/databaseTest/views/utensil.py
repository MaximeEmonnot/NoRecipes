from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from databaseTest.models import Utensil
import json

from utils import RunCypher, GetDataFromNode

# Récupération de tous les Ustensiles
@csrf_exempt
def get_all_utensils(request):
    if request.method == "GET":
        ustensiles = Utensil.nodes.all()
        data = [
            {
                "titre": ustensile.titre,
                "prix": ustensile.prix,
                "description": ustensile.description,
                "images": ustensile.images
            }
            for ustensile in ustensiles
        ]
        return JsonResponse({"ustensile": data}, safe=False)

# Récupération ustensile par le titre
@csrf_exempt
def get_utensil_by_title(request, title):
    if request.method == "GET":
        try:
            ustensile = Utensil.nodes.get(titre=title)
            data = {
               "titre": ustensile.titre,
               "prix": ustensile.prix,
               "description": ustensile.description,
               "images": ustensile.images
            }
            return JsonResponse({"utensile": data})
        except Utensil.DoesNotExist:
            return JsonResponse({"error": "Ustensile non trouvé"}, status=404)

# Ajout de ustensile
@csrf_exempt
def add_utensil(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            if not isinstance(data, dict):
                return JsonResponse({"error": "Le format est incorrect"}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Données invalides."}, status=400)


        #data = request.POST a utilisé quand le front end sera coder 

        titre = data.get("titre")
        prix = data.get("prix")
        description = data.get("description")
        images = data.get("images", "[]")  
        
        if not all([titre, prix, description]):
            return JsonResponse({"error": "Tous les champs sont requis."}, status=400)

        ustensile = Utensil(
            titre=titre,
            prix=prix,
            description=description,
            images=images
        )
        ustensile.save()

        return JsonResponse({"message": "Ustensile créé avec succès", "ustensile_id": ustensile.element_id})

# Modification ustensile
@csrf_exempt
def update_utensil(request, title):
    if request.method == "PUT":
        try:
            ustensile = Utensil.nodes.get(titre=title)
            data = json.loads(request.body)
            
            ustensile.prix = data.get("prix", ustensile.prix)
            ustensile.description = data.get("description", ustensile.description)
            ustensile.images = data.get("images", ustensile.images)
            
            ustensile.save()
            
            return JsonResponse({"message": "Ustensile mis à jour avec succès"})
        
        except Utensil.DoesNotExist:
            return JsonResponse({"error": "Ustensile non trouvé"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Données invalides"}, status=400)

# Suppression ustensile
@csrf_exempt
def delete_utensil(request, title):
    if request.method == "DELETE":
        try:
            ustensile = Utensil.nodes.get(titre=title)

            ustensile.delete()
            
            return JsonResponse({"message": "Ustensile supprimé avec succès"})
        
        except Utensil.DoesNotExist:
            return JsonResponse({"error": "Ustensile non trouvé"}, status=404)        


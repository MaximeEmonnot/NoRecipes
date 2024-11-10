from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from databaseTest.models import Utensile
import json

from utils import RunCypher, GetDataFromNode

# Récupération de tous les Ustensiles
@csrf_exempt
def get_all_utensiles(request):
    if request.method == "GET":
        utensiles = Utensile.nodes.all()
        data = [
            {
                "titre": utensile.titre,
                "prix": utensile.prix,
                "description": utensile.description,
                "images": utensile.images
            }
            for utensile in utensiles
        ]
        return JsonResponse({"ustensile": data}, safe=False)

# Récupération ustensile par le titre
@csrf_exempt
def get_utensile_by_title(request, title):
    if request.method == "GET":
        try:
            utensile = Utensile.nodes.get(titre=title)
            data = {
               "titre": utensile.titre,
               "prix": utensile.prix,
               "description": utensile.description,
               "images": utensile.images
            }
            return JsonResponse({"utensile": data})
        except Stensile.DoesNotExist:
            return JsonResponse({"error": "Ustensile non trouvé"}, status=404)

# Ajout de ustensile
@csrf_exempt
def add_utensile(request):
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

        utensile = Utensile(
            titre=titre,
            prix=prix,
            description=description,
            images=images
        )
        utensile.save()

        return JsonResponse({"message": "Ustensile créé avec succès", "utensile_id": utensile.element_id})

# Modification ustensile
@csrf_exempt
def update_utensile(request, title):
    if request.method == "PUT":
        try:
            utensile = Utensile.nodes.get(titre=title)
            data = json.loads(request.body)
            
            utensile.prix = data.get("prix", utensile.prix)
            utensile.description = data.get("description", utensile.description)
            utensile.images = data.get("images", utensile.images)
            
            utensile.save()
            
            return JsonResponse({"message": "Ustensile mis à jour avec succès"})
        
        except Utensile.DoesNotExist:
            return JsonResponse({"error": "Ustensile non trouvé"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Données invalides"}, status=400)

# Suppression ustensile
@csrf_exempt
def delete_utensile(request, title):
    if request.method == "DELETE":
        try:
            utensile = Utensile.nodes.get(titre=title)

            utensile.delete()
            
            return JsonResponse({"message": "Ustensile supprimé avec succès"})
        
        except Utensile.DoesNotExist:
            return JsonResponse({"error": "Ustensile non trouvé"}, status=404)        


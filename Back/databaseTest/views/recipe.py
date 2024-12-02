from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from databaseTest.models import Recipe
import json
import os
from neomodel import Q

from utils import RunCypher, GetDataFromNode

# Récupération de toutes les recettes
@csrf_exempt
def get_all_recipes(request):
    if request.method == "GET":
        print("Requête reçue pour récupérer les recettes")  
        recipes = Recipe.nodes.all()
        data = [
            {
                "titre": recipe.titre,
                "origine": recipe.origine,
                "note": recipe.note,
                "description": recipe.description,
                "images": recipe.images,
                "nombre_personnes": recipe.nombre_personnes,
                "temps_preparation": recipe.temps_preparation,
                "temps_cuisson": recipe.temps_cuisson,
                "temps_repos": recipe.temps_repos
            }
            for recipe in recipes
        ]
        return JsonResponse({"recipes": data}, safe=False)

# Récupération de recette par recherche simple
@csrf_exempt
def get_recipe_by_simple_search(request, search):
    if request.method == "GET" :
        try:
            recipe = Recipe.nodes.filter(
                  Q(titre__icontains=search)
                | Q(origine__icontains=search)
                | Q(description__icontains=search)
            )

            data = {
                "titre": recipe.titre,
                "origine": recipe.origine,
                "note": recipe.note,
                "description": recipe.description,
                "images": recipe.images,
                "nombre_personnes": recipe.nombre_personnes,
                "temps_preparation": recipe.temps_preparation,
                "temps_cuisson": recipe.temps_cuisson,
                "temps_repos": recipe.temps_repos
            }
            
            return JsonResponse({"recipe": data})
        except Recipe.DoesNotExist:
            return JsonResponse({"error" : "Recette non trouvée"}, status = 404)

# Récupération de recette par recherche avancée
@csrf_exempt
def get_recipe_by_advanced_search(request, search, ingredient_list, cuisine_type, origin, min_rate):
    if request.method == "GET":
        try:
            
            # Construction du path Ingredient
            ingredient_query = ""
            for ingredient in ingredient_list.split(","):
                ingredient_query += f", (r)-[CONTIENT]->(:Ingredient{{titre:{ingredient}}})"
                
            # Construction du path type de cuisine
            cuisine_type_query = ""
            if(cuisine_type):
                cuisine_type_query = f", (r)-[APPARTIENT_A]->(:Category{{titre:{cuisine_type}}})"
                
            query = "MATCH (r)" 
            + ingredient_query 
            + cuisine_type_query
            + f"WHERE r.origine = {origin} AND r.note >= {min_rate} AND r.titre CONTAINS {search}"
                
            answer, summary, keys = RunCypher(query)
            
            data = [GetDataFromNode(record) for record in answer]
            
            return JsonResponse({"recipes": data})
        except Recipe.DoesNotExist:
            return JsonResponse({"error" : "Recette non trouvée"}, status = 404)
        

# Récupération de recette par le titre
@csrf_exempt
def get_recipe_by_title(request, title):
    if request.method == "GET":
        try:
            recipe = Recipe.nodes.get(titre=title)
            data = {
               "titre": recipe.titre,
                "origine": recipe.origine,
                "note": recipe.note,
                "description": recipe.description,
                "images": recipe.images,
                "nombre_personnes": recipe.nombre_personnes,
                "temps_preparation": recipe.temps_preparation,
                "temps_cuisson": recipe.temps_cuisson,
                "temps_repos": recipe.temps_repos
            }
            return JsonResponse({"recipe": data})
        except Recipe.DoesNotExist:
            return JsonResponse({"error": "Recette non trouvée"}, status=404)

# Ajout de recette
@csrf_exempt
def add_recipe(request):
    if request.method == "POST":
        try: 
            titre = request.POST.get("titre")
            origine = request.POST.get("origine")
            description = request.POST.get("description")
            nombre_personnes = int(request.POST.get("nombrePersonnes", 1))
            temps_preparation = int(request.POST.get("tempsPreparation", 0))
            temps_cuisson = int(request.POST.get("tempsCuisson", 0))
            temps_repos = int(request.POST.get("tempsRepos", 1))
            
            if not all([titre, origine, description, temps_preparation, temps_cuisson, nombre_personnes]):
                return JsonResponse({"error": "Tous les champs sont requis."}, status=400)

            recipe = Recipe(
                titre=titre,
                origine=origine,
                description=description,
                nombre_personnes=nombre_personnes,
                temps_preparation=temps_preparation,
                temps_cuisson=temps_cuisson,
                temps_repos=temps_repos
            )
            recipe.save()

              # Gestion des fichiers (images)
            images = request.FILES.getlist("images")  
            image_urls = []

            # Chemin vers le répertoire media
            media_path = "media/recipes"
            if not os.path.exists(media_path): 
                os.makedirs(media_path)

            for image in images:
                image_name = f"recipes/{image.name}"
                image_urls.append(image_name)

                with open(f"media/{image_name}", "wb+") as destination:
                    for chunk in image.chunks():
                        destination.write(chunk)

            # Ajout des images à la recette
            recipe.images = image_urls
            recipe.save()

            return JsonResponse({"message": "Recette créée avec succès", "recipe_id": recipe.element_id})

        except Exception as e:
            return JsonResponse({"error": f"Erreur lors de la création de la recette : {str(e)}"}, status=500)

# Modification recette
@csrf_exempt
def update_recipe(request, title):
    if request.method == "PUT":
        try:
            recipe = Recipe.nodes.get(titre=title)
            data = json.loads(request.body)
            
            recipe.origine = data.get("origine", recipe.origine)
            recipe.description = data.get("description", recipe.description)
            recipe.images = data.get("images", recipe.images)
            recipe.nombre_personnes = data.get("nombre_personnes", recipe.nombre_personnes)
            recipe.temps_preparation = data.get("temps_preparation", recipe.temps_preparation)
            recipe.temps_cuisson = data.get("temps_cuisson", recipe.temps_cuisson)
            recipe.nombre_personnes = data.get("temps_repos", recipe.temps_repos)
            
            recipe.save()
            
            return JsonResponse({"message": "Recette mise à jour avec succès"})
        
        except Recipe.DoesNotExist:
            return JsonResponse({"error": "Recette non trouvée"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Données invalides"}, status=400)

# Suppression recette
@csrf_exempt
def delete_recipe(request, title):
    if request.method == "DELETE":
        try:
            recipe = Recipe.nodes.get(titre=title)

            recipe.delete()
            
            return JsonResponse({"message": "Recette supprimée avec succès"})
        
        except Recipe.DoesNotExist:
            return JsonResponse({"error": "Recette non trouvée"}, status=404)        


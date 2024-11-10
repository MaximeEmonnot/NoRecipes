from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from databaseTest.models import Recipe
import json

from utils import RunCypher, GetDataFromNode

# Récupération de toutes les recettes
@csrf_exempt
def get_all_recipes(request):
    if request.method == "GET":
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
            data = json.loads(request.body)
            # Vérification si data est un dictionnaire et pas une liste pour bien gérer la liste des images
            if not isinstance(data, dict):
                return JsonResponse({"error": "Le format est incorrect"}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Données invalides."}, status=400)


        #data = request.POST a utilisé quand le front end sera coder

        titre = data.get("titre")
        origine = data.get("origine")
        description = data.get("description")
        nombre_personnes = int(data.get("nombrePersonnes", 1))
        temps_preparation = int(data.get("tempsPreparation", 0))
        temps_cuisson = int(data.get("tempsCuisson", 0))
        temps_repos = int(data.get("tempsRepos", 1))

        images = data.get("images", "[]")  
        
        if not all([titre, origine, description, temps_preparation, temps_cuisson, nombre_personnes]):
            return JsonResponse({"error": "Tous les champs sont requis."}, status=400)

        """existing_recipe = Recipe.nodes.filter(titre=titre).first()
        if existing_recipe is not None:
            return JsonResponse({"error": "Une recette avec ce titre existe déjà."}, status=400)"""

        recipe = Recipe(
            titre=titre,
            origine=origine,
            description=description,
            nombre_personnes=nombre_personnes,
            temps_preparation=temps_preparation,
            temps_cuisson=temps_cuisson,
            temps_repos=temps_repos,
            images=images
        )
        recipe.save()

        return JsonResponse({"message": "Recette créée avec succès", "recipe_id": recipe.element_id})

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


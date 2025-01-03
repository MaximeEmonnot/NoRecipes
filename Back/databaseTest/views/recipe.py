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
                "temps_cuisson": recipe.temps_cuisson
            }
            for recipe in recipes
        ]
        return JsonResponse({"recipes": data}, safe=False)

# Récupération de recette par recherche simple
@csrf_exempt
def get_recipe_by_simple_search(request, search):
    if request.method == "GET" :
        try:
            recipes = Recipe.nodes.filter(
                  Q(titre__icontains=search)
                | Q(origine__icontains=search)
                | Q(description__icontains=search)
            )

            data = [
                {
                "titre": recipe.titre,
                "origine": recipe.origine,
                "note": recipe.note,
                "description": recipe.description,
                "images": recipe.images,
                "nombre_personnes": recipe.nombre_personnes,
                "temps_preparation": recipe.temps_preparation,
                "temps_cuisson": recipe.temps_cuisson
                }
                for recipe in recipes
            ]
            
            return JsonResponse({"recipes": data})
        except Recipe.DoesNotExist:
            return JsonResponse({"error" : "Recette non trouvée"}, status = 404)

# Récupération de recette par recherche avancée
@csrf_exempt
def get_recipe_by_advanced_search(request):
    if request.method == "GET":
        try:
            search          = request.GET.get("search")
            ingredient_list = request.GET.get("ingredient_list")
            cuisine_type    = request.GET.get("cuisine_type")
            origin          = request.GET.get("origin")
            min_rate        = request.GET.get("min_rate")
            
            # Construction du path Ingredient
            ingredient_query = ""
            if(ingredient_list):
                for ingredient in ingredient_list.split(","):
                    ingredient_query += f", (r)-[:CONTIENT]->(:Ingredient{{titre:'{ingredient}'}})"
                
            # Construction du path type de cuisine
            cuisine_type_query = ""
            if(cuisine_type):
                cuisine_type_query = f", (r)-[:APPARTIENT_A]->(:Category{{titre:'{cuisine_type}'}})"
                
            # Construction de la clause WHERE
            where_query = ""
            if(search or origin or min_rate):
                where_query = "WHERE "
                if(search):
                    where_query += f"LOWER(r.titre) CONTAINS LOWER('{search}') "
                    if(origin or min_rate):
                        where_query += "AND "
                if (origin):
                    where_query += f"r.origine = '{origin}' "
                    if (min_rate):
                        where_query += "AND "
                if(min_rate):
                    where_query += f"r.note >= {min_rate} "
                
            query = "MATCH (r:Recipe)" + ingredient_query + cuisine_type_query + where_query + "RETURN r"
                
            answer, summary, keys = RunCypher(query)
            
            data = [GetDataFromNode(record) for record in answer]
            
            return JsonResponse({"recipes": data})
        except Recipe.DoesNotExist:
            return JsonResponse({"error" : "Recette non trouvée"}, status = 404)

# Récupération des recherches correspondant à la recherche en cours (recommandation)
@csrf_exempt
def get_recommanded_recipes(request):
    if request.method == "GET":
        try:
            current_recipe  = request.GET.get("current")
            ingredient_list = request.GET.get("ingredient_list")
            cuisine_type    = request.GET.get("cuisine_type")
            origin          = request.GET.get("origin")
            
            # Construction du path Ingredient
            ingredient_query = ""
            ing_index = 0
            for ingredient in ingredient_list.split(","):
                ingredient_query += f" OPTIONAL MATCH (r)-[:CONTIENT]->({chr(ord('a') + ing_index)}:Ingredient{{titre:'{ingredient}'}})"
                ing_index += 1
            
            # Contruction de la clause WHERE additionnelle pour les ingrédients
            ingredient_with_query = ""
            if(ing_index > 0):
                ingredient_with_query = " WITH r, COUNT(a) AS num_a"
                for i in range(1, ing_index):
                    ingredient_with_query += f", COUNT({chr(ord('a') + i)}) AS num_{chr(ord('a') + i)}"
                ingredient_with_query += " WHERE num_a"
                for i in range(1, ing_index):
                    ingredient_with_query += f" + num_{chr(ord('a') + i)}"
                ingredient_with_query += " > 0"
                
            # Construction du path type de cuisine
            cuisine_type_query = ""
            if(cuisine_type):
                cuisine_type_query = f" OPTIONAL MATCH (r)-[:APPARTIENT_A]->(:Category{{titre:'{cuisine_type}'}})"
                
            # Construction de la clause WHERE
            where_query = ""
            if(origin and current_recipe):
                where_query = f" WHERE r.origine = '{origin}' AND r.titre <> '{current_recipe}'"
                
            query = "MATCH (r:Recipe)" + where_query + ingredient_query + cuisine_type_query + ingredient_with_query + " RETURN DISTINCT r ORDER BY r.note DESC LIMIT 3"
                
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
                "temps_cuisson": recipe.temps_cuisson
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

            if not all([titre, origine, description, temps_preparation, temps_cuisson, nombre_personnes]):
                return JsonResponse({"error": "Tous les champs sont requis."}, status=400)

            recipe = Recipe(
                titre=titre,
                origine=origine,
                description=description,
                nombre_personnes=nombre_personnes,
                temps_preparation=temps_preparation,
                temps_cuisson=temps_cuisson
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

            data = request.POST
            recipe.origine = data.get("origine", recipe.origine)
            recipe.description = data.get("description", recipe.description)
            recipe.nombre_personnes = data.get("nombre_personnes", recipe.nombre_personnes)
            recipe.temps_preparation = data.get("temps_preparation", recipe.temps_preparation)
            recipe.temps_cuisson = data.get("temps_cuisson", recipe.temps_cuisson)
            
             # Gestion des nouvelles images
            images = request.FILES.getlist("images") 
            if images:
                image_urls = []

                media_path = "media/recipes"
                if not os.path.exists(media_path):
                    os.makedirs(media_path)

                for image in images:
                    image_name = f"recipes/{image.name}"
                    image_urls.append(image_name)

                    with open(f"media/{image_name}", "wb+") as destination:
                        for chunk in image.chunks():
                            destination.write(chunk)

                recipe.images = image_urls

            recipe.save()

            return JsonResponse({"message": "Recette mise à jour avec succès"})

        except Recipe.DoesNotExist:
            return JsonResponse({"error": "Recette non trouvée"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Données invalides."}, status=400)
        except Exception as e:
            return JsonResponse({"error": f"Erreur lors de la mise à jour de la recette : {str(e)}"}, status=500)

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


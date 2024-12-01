from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from databaseTest.models import Comments, Recipe
import json

from utils import RunCypher, GetDataFromNode

# Ajout d"un commentaire
@csrf_exempt
def add_comment(request, recipe_title):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            texte = data.get("texte")
            images = data.get("images", [])

            if not texte:
                return JsonResponse({"error": "Veuillez laisser un commentaire."}, status=400)

            try:
                recipe = Recipe.nodes.get(titre=recipe_title)
            except Recipe.DoesNotExist:
                return JsonResponse({"error": "Recette non trouvée."}, status=404)

            commentaire = Comments(texte=texte, images=images)
            commentaire.save()
            commentaire.recette.connect(recipe)

            return JsonResponse({"message": "Commentaire ajouté avec succès", "comment_id": commentaire.uuid})
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Données invalides."}, status=400)

# Récupérer un commentaire
@csrf_exempt
def get_comment(request, comment_id):
    if request.method == "GET":
        try:
            commentaire = Comments.nodes.get(uuid=comment_id)
            data = {
                "texte": commentaire.texte,
                "images": commentaire.images
            }
            return JsonResponse({"commentaire": data})
        except Comments.DoesNotExist:
            return JsonResponse({"error": "Commentaire non trouvé"}, status=404)

# Récupérer tous les commentaires d'une recette
@csrf_exempt
def get_all_comments(request, recipe_title):
    if request.method == "GET":
        try:
            recipe = Recipe.nodes.get(titre=recipe_title)
            commentaires = recipe.commentaires.all()

            data = [
                {
                    "texte": commentaire.texte,
                    "images": commentaire.images
                }
                for commentaire in commentaires
            ]
            return JsonResponse({"commentaires": data})
        except Recipe.DoesNotExist:
            return JsonResponse({"error": "Recette non trouvée"}, status=404)

#Modification d'un commentaire
@csrf_exempt
def update_comment(request, comment_id):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            commentaire = Comments.nodes.get(uuid=comment_id)
            
            commentaire.texte = data.get("texte", commentaire.texte)
            commentaire.images = data.get("images", commentaire.images)
            commentaire.save()
            
            return JsonResponse({"message": "Commentaire mis à jour avec succès"})
        
        except Comments.DoesNotExist:
            return JsonResponse({"error": "Commentaire non trouvé"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Données invalides."}, status=400)


# Suppression Catégorie
@csrf_exempt
def delete_comment(request, comment_id):
    if request.method == "DELETE":
        try:
            commentaire = Comments.nodes.get(uuid=comment_id)
            commentaire.delete()
            return JsonResponse({"message": "Commentaire supprimé avec succès"})
        except Comments.DoesNotExist:
            return JsonResponse({"error": "Commentaire non trouvé"}, status=404)
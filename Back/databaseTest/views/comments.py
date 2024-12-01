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
            note = data.get("note")

            if not texte:
                return JsonResponse({"error": "Veuillez laisser un commentaire."}, status=400)
            if not note or not (1 <= note <= 5):
                return JsonResponse({"error": "Veuillez noter la recette entre 1 et 5."}, status=400)


            try:
                recipe = Recipe.nodes.get(titre=recipe_title)
            except Recipe.DoesNotExist:
                return JsonResponse({"error": "Recette non trouvée."}, status=404)

            commentaire = Comments(texte=texte, images=images, note=note)
            commentaire.save()
            commentaire.recette.connect(recipe)

            # Mettre à jour la moyenne des notes
            recipe.total_notes += 1
            recipe.somme_notes += note
            recipe.note = recipe.somme_notes / recipe.total_notes
            recipe.save()

            return JsonResponse({
                "message": "Commentaire ajouté avec succès",
                "note_moyenne": recipe.note,
                "comment_id": commentaire.uuid
                })
        
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
                "note": comment.note,
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
                    "note": commentaire.note,
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
            commentaire.note = data.get("note", commentaire.note)
            commentaire.images = data.get("images", commentaire.images)
            commentaire.save()
            
            return JsonResponse({"message": "Commentaire mis à jour avec succès"})
        
        except Comments.DoesNotExist:
            return JsonResponse({"error": "Commentaire non trouvé"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Données invalides."}, status=400)


# Suppression Catégorie
@csrf_exempt
def delete_comment(request, recette_title, comment_id):
    if request.method == "DELETE":
        try:
            recipe = Recette.nodes.get(titre=recette_title)
            commentaire = Comments.nodes.get(uuid=comment_id)

            if not recipe.commentaires.is_connected(commentaire):
                return JsonResponse({"error": "Le commentaire n'est pas lié à cette recette."}, status=400)

            recipe.commentaires.disconnect(commentaire)

            # Mettre à jour la moyenne des notes
            recipe.total_notes -= 1
            recipe.somme_notes -= commentaire.note
            recipe.note = recipe.somme_notes / recipe.total_notes if recipe.total_notes > 0 else 0.0
            recipe.save()

            commentaire.delete()

            return JsonResponse({"message": "Commentaire supprimé avec succès"})
        except Comments.DoesNotExist:
            return JsonResponse({"error": "Commentaire non trouvé"}, status=404)
from django.db import models
import uuid
from neomodel import StructuredNode, ArrayProperty, StringProperty, IntegerProperty, FloatProperty, JSONProperty, RelationshipTo, RelationshipFrom, UniqueIdProperty, StructuredRel

# Create your models here.

# Relation entre Recette et Ingrédient
class Contient(StructuredRel):
    quantite = FloatProperty()
    # type = EnumProperty(UnitIngredient)
    type_unite = StringProperty(choices={
        "g": "Grammes",
        "ml": "Millilitres",
        "l": "Litres",
        "cs": "Cuillère à soupe",
        "cc": "Cuillère à café"
    })

# Relation entre Recette et Ustensile
class Utilise(StructuredRel):
    nombre = IntegerProperty(default=1)

class Comments(StructuredNode):
    uuid = UniqueIdProperty()
    texte = StringProperty()
    images = JSONProperty(default=[])
    note = IntegerProperty(required=True, choices=range(1, 6))  # Note entre 1 et 5

    # Relation avec recette 
    recette = RelationshipFrom('Recipe', 'POSSEDE')

class Utensil(StructuredNode):
    titre = StringProperty(unique_index=True, required=True)
    description = StringProperty()
    prix = FloatProperty()
    images = JSONProperty()

    # Relation avec recette avec la relation UTILISE
    ustensiles = RelationshipFrom('Recipe', 'UTILISE', model=Utilise)

class Ingredient(StructuredNode):
    titre = StringProperty(unique_index=True, required=True)
    description = StringProperty()
    prix = FloatProperty()
    images = JSONProperty()

    # Relation avec Recipe avec la relation CONTIENT
    recettes = RelationshipFrom('Recipe', 'CONTIENT', model=Contient)

class Recipe(StructuredNode):
    titre = StringProperty(unique_index=True, required=True)
    origine = StringProperty() 
    note = FloatProperty(default=0.0)  # Note moyenne
    total_notes = IntegerProperty(default=0)  # Nombre de notes reçues
    somme_notes = IntegerProperty(default=0)  # Somme des notes pour calculer la moyenne
    description = StringProperty()
    images = ArrayProperty()
    nombre_personnes = IntegerProperty()
    temps_preparation = IntegerProperty()
    temps_cuisson = IntegerProperty()
    temps_repos = IntegerProperty()

    # Relation recette - catégorie
    categorie = RelationshipTo('Category', 'APPARTIENT_A')

    # Relation vers Ingredient avec la relation CONTIENT
    ingredients = RelationshipTo('Ingredient', 'CONTIENT', model=Contient)

    # Relation vers ustensile avec la relation UTILISE
    ustensiles = RelationshipTo('Utensil', 'UTILISE', model=Utilise)

    # Relation avec commentaires
    commentaires = RelationshipTo('Comments', 'POSSEDE')

class Category(StructuredNode):
    titre = StringProperty(unique_index=True, required=True)
    images = ArrayProperty()

    # Relation catégorie - recette
    recettes = RelationshipFrom('Recipe', 'APPARTIENT_A')

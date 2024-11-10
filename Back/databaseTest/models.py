from django.db import models
from neomodel import StructuredNode, StringProperty, IntegerProperty, FloatProperty, JSONProperty, RelationshipTo, RelationshipFrom

# Create your models here.
class Recipe(StructuredNode):
    titre = StringProperty(unique_index=True, required=True)
    origine = StringProperty()
    note = FloatProperty(default=0.0)
    description = StringProperty()
    images = JSONProperty()
    nombre_personnes = IntegerProperty()
    temps_preparation = IntegerProperty()
    temps_cuisson = IntegerProperty()
    temps_repos = IntegerProperty()

class Ingredient(StructuredNode):
    titre = StringProperty(unique_index=True, required=True)
    description = StringProperty()
    prix = FloatProperty()
    images = JSONProperty()

class Utensile(StructuredNode):
    titre = StringProperty(unique_index=True, required=True)
    description = StringProperty()
    prix = FloatProperty()
    images = JSONProperty()
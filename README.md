# Projet Warehousing, Data Lakes, Polystores

Projet réalisé dans le cadre de la 2ème année de Master DS4SC

Réalisé par : 
- Therno Amadou DIALLO
- Maxime EMONNOT
- Maimouna TIMERA

## Objectif du projet

Concevoir une solution efficace pour gérer ces données interconnectées tout en faisant une prise en main de Neo4j et en exploitant ses capacités.

## Choix technologiques

| Back-end | Front-end | Base de données |
|----------|-----------|-----------------|
| Django   | React     | Neo4J           |


## Récupération des données

Le fichier Cypher, contenant les scripts nécessaires pour alimenter la base de données Neo4j, est disponible dans le répertoire suivant :
Back/databaseTest/Données.

Note : Ce fichier doit être exécuté dans Neo4j pour initialiser les données avant de lancer l'application.

## Instruction pour lancer l'application 

# A faire sur Neo4J
Après avoir importé le fichier Cypher dans Neo4j, vous devez ajuster un paramètre. Pour ce faire :

- Cliquer sur les trois petits points (...) en haut à droite, puis sélectionnez Settings :
<img width="665" alt="image" src="https://github.com/user-attachments/assets/9e62d589-5f91-498a-8487-77a5c8db2937">

- Faites défiler jusqu'au paramètre *dbms.security.auth_enabled* et définissez-le sur **false** :
<img width="713" alt="image" src="https://github.com/user-attachments/assets/4c2ec585-51fa-4e0a-8db8-7486598ada35">



# A faire sur le Back
- Ouvrir un terminal dans le dossier back
- Exécuter la commande "**pip install -r requirements.txt**"
- Ensuite exécuter la commande **python manage.py runserver** pour lancer le serveur

# A faire sur le front
Exécuter la commande "npm start" dans un terminal intégré, à partir du répertoire front.

Note : Si nécessaire, exécutez d'abord la commande suivante pour installer les dépendances :




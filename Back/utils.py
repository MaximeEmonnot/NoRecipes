from neo4j import GraphDatabase, Record

URI  = "bolt://localhost:7687/"
AUTH = ("neo4j", "neo4j")
 
with GraphDatabase.driver(URI) as driver:
    driver.verify_connectivity()
    
def RunCypher(query, parameters : dict | None = None):
    """
        Retourne le résultat de la requête CYPHER
        
        Les record peuvent être utilisés en utilisant :\n
            for record in result
            
        Le traitement de chaque record devra être fait au cas par cas, mais voici quelques exemples :\n
        
            * Si la requête renvoie un objet entier (ex: MATCH (n) RETURN n), il est possible de récupérer l\'ensemble des attributs de l\'objet de la manière suivante : \n
                list(record.data().values())[0] 
                
                Explication :                 
                record.data().values() renvoie un objet dict_values
                list() permet de le transformer en une liste de dict (contenant un seul dict)
                Ici on récupère donc l'unique dict
            * Si la requête ne renvoie qu'un seul attribut (ex: MATCH(n:Person) RETURN n.name), on peut récupérer l'attribut unique de la manière suivante :
                record.single()
                
        Dans les deux exemples ci-dessus, récupérer les valeurs se fait via des opérations sur des object dict
    """
    records, summary, keys = driver.execute_query(query_ = query, parameters_ = parameters, database_ = "neo4j")

    return records, summary, keys
    
def GetDataFromNode(node : Record) -> dict[str : any]:
    return list(node.data().values())[0]

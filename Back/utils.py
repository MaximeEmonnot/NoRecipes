from pymongo import MongoClient

def GetDBHandle(db_name, host, port, username, password):
    
    client = MongoClient(host = host,
                         port = int(port),
                         username = username,
                         password = password
                         )
    
    db_handle = client[db_name]
    
    return db_handle, client
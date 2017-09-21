from pymongo import MongoClient

def getConnection():
    uri = "mongodb://miletrav:4510045100x!@compute.miletrav.com/miletrav-development?authMechanism=SCRAM-SHA-1&authSource=admin"
    client = MongoClient(uri)
    return client

def saveMovieRecommender(data, client):
    collection = client['miletrav-development'].RC_Movie
    collection.save(data)

def saveActivityRecommender(data, client):
    collection = client['miletrav-development'].Miletrav_RC
    collection.save(data)

def clearMovieRecommendation(client):
    collection = client['miletrav-development'].RC_Movie
    collection.remove({})

def clearActivityRecommendation(client):
    collection = client['miletrav-development'].Miletrav_RC
    collection.remove({})
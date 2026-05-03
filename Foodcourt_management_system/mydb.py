import pymongo
def start_db():
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    db=client["university_db"]
    return db